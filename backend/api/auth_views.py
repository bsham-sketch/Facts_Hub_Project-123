"""
Authentication views for the Facts Hub API
Handles registration, login, logout, password reset, email verification
"""
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.conf import settings
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import logging

from .models import CustomUser, LoginAttempt
from .serializers import (
    RegisterSerializer, 
    LoginSerializer, 
    UserSerializer,
    PasswordResetSerializer,
    SetPasswordSerializer,
    ChangePasswordSerializer,
    EmailVerificationSerializer
)
from .email_service import (
    send_email_verification_email,
    send_password_reset_email,
    send_welcome_email
)
from .permissions import IsOwnerOrReadOnly

logger = logging.getLogger(__name__)


@method_decorator(csrf_protect, name='dispatch')
class RegisterView(generics.CreateAPIView):
    """
    Register a new user
    POST /api/auth/register/
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = serializer.save()
            
            # Generate email verification token
            token = user.generate_email_verification_token()
            
            # Send verification email
            email_sent = send_email_verification_email(user, token)
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'message': 'Registration successful. Please check your email to verify your account.',
                'user': UserSerializer(user).data,
                'email_sent': email_sent,
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            logger.error(f"Registration error: {str(e)}")
            return Response(
                {'error': 'Registration failed. Please try again.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    """
    Login user and return JWT tokens
    POST /api/auth/login/
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        ip_address = self.get_client_ip(request)
        
        # Check for account lockout
        try:
            user = CustomUser.objects.get(email=email)
            
            if user.is_locked_out():
                remaining_time = (user.locked_until - timezone.now()).seconds // 60
                return Response(
                    {
                        'error': f'Account is temporarily locked. Please try again in {remaining_time} minutes.',
                        'locked_until': user.locked_until.isoformat()
                    },
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )
            
        except CustomUser.DoesNotExist:
            # Don't reveal if user exists or not
            return Response(
                {'error': 'Invalid email or password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Authenticate user
        user = authenticate(email=email, password=password)
        
        if user is None:
            # Increment failed login attempts
            try:
                user = CustomUser.objects.get(email=email)
                user.increment_failed_login_attempts()
            except CustomUser.DoesNotExist:
                pass
            
            # Log failed attempt
            LoginAttempt.objects.create(
                ip_address=ip_address,
                email=email,
                success=False
            )
            
            return Response(
                {'error': 'Invalid email or password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Check if email is verified
        if not user.is_email_verified:
            return Response(
                {
                    'error': 'Please verify your email address before logging in.',
                    'email': user.email
                },
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Reset failed login attempts
        user.reset_failed_login_attempts()
        
        # Log successful attempt
        LoginAttempt.objects.create(
            ip_address=ip_address,
            email=email,
            success=True
        )
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        # Set refresh token in HTTP-only cookie
        response = Response({
            'message': 'Login successful.',
            'user': UserSerializer(user).data,
            'access_token_expires_in': int(settings.JWT_ACCESS_TOKEN_LIFETIME.total_seconds()),
        }, status=status.HTTP_200_OK)
        
        # Set refresh token in HTTP-only cookie
        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Lax',
            max_age=int(settings.JWT_REFRESH_TOKEN_LIFETIME.total_seconds()),
        )
        
        return response
    
    def get_client_ip(self, request):
        """Get client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


@method_decorator(csrf_protect, name='dispatch')
class LogoutView(APIView):
    """
    Logout user and blacklist refresh token
    POST /api/auth/logout/
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            
            response = Response(
                {'message': 'Logout successful.'},
                status=status.HTTP_200_OK
            )
            
            # Clear refresh token cookie
            response.delete_cookie('refresh_token')
            
            return response
            
        except TokenError:
            return Response(
                {'error': 'Invalid token.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Logout error: {str(e)}")
            return Response(
                {'error': 'Logout failed.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_protect, name='dispatch')
class VerifyEmailView(APIView):
    """
    Verify user's email address
    GET /api/auth/verify-email/<token>/
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, token, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email_verification_token=token)
            
            if user.verify_email_token(token):
                user.verify_email()
                send_welcome_email(user)
                
                return Response({
                    'message': 'Email verified successfully. You can now log in.'
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'error': 'Invalid or expired verification token.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Invalid verification token.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Email verification error: {str(e)}")
            return Response(
                {'error': 'Email verification failed.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_protect, name='dispatch')
class ResendVerificationEmailView(APIView):
    """
    Resend verification email
    POST /api/auth/resend-verification-email/
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        
        if not email:
            return Response(
                {'error': 'Email is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = CustomUser.objects.get(email=email)
            
            if user.is_email_verified:
                return Response(
                    {'message': 'Email is already verified.'},
                    status=status.HTTP_200_OK
                )
            
            # Generate new token
            token = user.generate_email_verification_token()
            
            # Send verification email
            email_sent = send_email_verification_email(user, token)
            
            return Response({
                'message': 'Verification email sent.',
                'email_sent': email_sent
            }, status=status.HTTP_200_OK)
            
        except CustomUser.DoesNotExist:
            # Don't reveal if user exists
            return Response(
                {'message': 'If the email exists, a verification link has been sent.'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f"Resend verification error: {str(e)}")
            return Response(
                {'error': 'Failed to send verification email.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_protect, name='dispatch')
class ForgotPasswordView(APIView):
    """
    Send password reset email
    POST /api/auth/forgot-password/
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        
        try:
            user = CustomUser.objects.get(email=email)
            
            # Generate password reset token
            token = user.generate_password_reset_token()
            
            # Send reset email
            email_sent = send_password_reset_email(user, token)
            
            return Response({
                'message': 'If the email exists, a password reset link has been sent.',
                'email_sent': email_sent
            }, status=status.HTTP_200_OK)
            
        except CustomUser.DoesNotExist:
            # Don't reveal if user exists
            return Response(
                {'message': 'If the email exists, a password reset link has been sent.'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f"Forgot password error: {str(e)}")
            return Response(
                {'error': 'Failed to process request.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_protect, name='dispatch')
class ResetPasswordView(APIView):
    """
    Reset password using token
    POST /api/auth/reset-password/
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = SetPasswordSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = SetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['password']
        
        try:
            user = CustomUser.objects.get(password_reset_token=token)
            
            if user.verify_password_reset_token(token):
                user.set_password(new_password)
                user.invalidate_password_reset_token()
                user.save()
                
                return Response({
                    'message': 'Password reset successful. You can now log in.'
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'error': 'Invalid or expired reset token.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Invalid reset token.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Reset password error: {str(e)}")
            return Response(
                {'error': 'Password reset failed.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_protect, name='dispatch')
class ChangePasswordView(APIView):
    """
    Change password for authenticated user
    POST /api/auth/change-password/
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']
        
        if not user.check_password(old_password):
            return Response(
                {'error': 'Current password is incorrect.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            validate_password(new_password, user=user)
        except ValidationError as e:
            return Response(
                {'error': list(e.messages)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.set_password(new_password)
        user.save()
        
        return Response({
            'message': 'Password changed successfully.'
        }, status=status.HTTP_200_OK)


@method_decorator(csrf_protect, name='dispatch')
class CurrentUserView(APIView):
    """
    Get current user information
    GET /api/auth/me/
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)
    
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@method_decorator(csrf_protect, name='dispatch')
class RefreshTokenView(APIView):
    """
    Refresh access token using refresh token from cookie
    POST /api/auth/refresh/
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            return Response(
                {'error': 'Refresh token not found.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
            
            return Response({
                'access_token': access_token,
                'token_type': 'Bearer',
                'expires_in': int(settings.JWT_ACCESS_TOKEN_LIFETIME.total_seconds()),
            }, status=status.HTTP_200_OK)
            
        except TokenError as e:
            return Response(
                {'error': 'Invalid or expired refresh token.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            logger.error(f"Refresh token error: {str(e)}")
            return Response(
                {'error': 'Token refresh failed.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )