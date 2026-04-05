from django.urls import path
from . import views
from .views import facts_list, categories_list, facts_by_category
from .auth_views import (
    RegisterView,
    LoginView,
    LogoutView,
    VerifyEmailView,
    ResendVerificationEmailView,
    ForgotPasswordView,
    ResetPasswordView,
    ChangePasswordView,
    CurrentUserView,
    RefreshTokenView,
)

urlpatterns = [
    # API Root
    path('', views.ApiRootView.as_view(), name='api-root'),
    
    # Facts endpoints
    path('categories/', categories_list, name='categories-list'),
    path('facts/', facts_list, name='facts-list'),
    path('facts/category/<str:category>/', facts_by_category, name='facts-by-category'),
    path('facts/<int:fact_id>/', views.FactDetailView.as_view(), name='fact-detail'),
    path('facts/add/', views.AddFactView.as_view(), name='fact-add'),
    
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/verify-email/<str:token>/', VerifyEmailView.as_view(), name='auth-verify-email'),
    path('auth/resend-verification-email/', ResendVerificationEmailView.as_view(), name='auth-resend-verification'),
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='auth-forgot-password'),
    path('auth/reset-password/', ResetPasswordView.as_view(), name='auth-reset-password'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='auth-change-password'),
    path('auth/me/', CurrentUserView.as_view(), name='auth-current-user'),
    path('auth/refresh/', RefreshTokenView.as_view(), name='auth-refresh'),
]