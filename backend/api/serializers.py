"""
Serializers for authentication
"""
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user data"""
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_email_verified', 'date_joined']
        read_only_fields = ['id', 'is_email_verified', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password_confirm', 'first_name', 'last_name']
    
    def validate_email(self, value):
        """Check if email already exists"""
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('A user with this email already exists.')
        return value
    
    def validate(self, attrs):
        """Validate password confirmation"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password_confirm': 'Passwords do not match.'})
        return attrs
    
    def create(self, validated_data):
        """Create user with hashed password"""
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    
    def validate_email(self, value):
        """Validate email exists"""
        if not CustomUser.objects.filter(email=value).exists():
            # Don't reveal if user exists
            return value
        return value


class PasswordResetSerializer(serializers.Serializer):
    """Serializer for forgot password"""
    email = serializers.EmailField(required=True)


class SetPasswordSerializer(serializers.Serializer):
    """Serializer for setting new password with token"""
    token = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        """Validate password confirmation"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password_confirm': 'Passwords do not match.'})
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for changing password"""
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    new_password_confirm = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        """Validate password confirmation"""
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({'new_password_confirm': 'Passwords do not match.'})
        
        # Check if new password is same as old password
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({'new_password': 'New password must be different from current password.'})
        
        return attrs


class EmailVerificationSerializer(serializers.Serializer):
    """Serializer for email verification"""
    token = serializers.CharField(required=True)