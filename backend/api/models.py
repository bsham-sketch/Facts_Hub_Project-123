from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta
import secrets
import hashlib


class CustomUser(AbstractUser):
    """Custom user model with email verification and account lockout"""
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=255, blank=True, null=True)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)
    password_reset_token_created = models.DateTimeField(blank=True, null=True)
    
    # Account lockout fields
    failed_login_attempts = models.IntegerField(default=0)
    locked_until = models.DateTimeField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Required for AbstractUser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def generate_email_verification_token(self):
        """Generate a secure token for email verification"""
        self.email_verification_token = secrets.token_urlsafe(32)
        self.save(update_fields=['email_verification_token'])
        return self.email_verification_token
    
    def generate_password_reset_token(self):
        """Generate a secure token for password reset"""
        self.password_reset_token = secrets.token_urlsafe(32)
        self.password_reset_token_created = timezone.now()
        self.save(update_fields=['password_reset_token', 'password_reset_token_created'])
        return self.password_reset_token
    
    def verify_email_token(self, token):
        """Verify email verification token"""
        return self.email_verification_token == token
    
    def verify_password_reset_token(self, token):
        """Verify password reset token is valid and not expired"""
        if not self.password_reset_token or not self.password_reset_token_created:
            return False
        
        # Check if token matches
        if self.password_reset_token != token:
            return False
        
        # Check if token is expired (15 minutes)
        token_age = timezone.now() - self.password_reset_token_created
        if token_age > timedelta(minutes=15):
            self.invalidate_password_reset_token()
            return False
        
        return True
    
    def invalidate_password_reset_token(self):
        """Invalidate the password reset token (one-time use)"""
        self.password_reset_token = None
        self.password_reset_token_created = None
        self.save(update_fields=['password_reset_token', 'password_reset_token_created'])
    
    def verify_email(self):
        """Mark email as verified"""
        self.is_email_verified = True
        self.email_verification_token = None
        self.save(update_fields=['is_email_verified', 'email_verification_token'])
    
    def is_locked_out(self):
        """Check if account is locked due to failed login attempts"""
        if not self.locked_until:
            return False
        return timezone.now() < self.locked_until
    
    def increment_failed_login_attempts(self):
        """Increment failed login attempts and lock account if threshold reached"""
        self.failed_login_attempts += 1
        
        if self.failed_login_attempts >= 5:
            from django.conf import settings
            lockout_minutes = settings.ACCOUNT_LOCKOUT_DURATION_MINUTES
            self.locked_until = timezone.now() + timedelta(minutes=lockout_minutes)
        
        self.save(update_fields=['failed_login_attempts', 'locked_until'])
    
    def reset_failed_login_attempts(self):
        """Reset failed login attempts after successful login"""
        self.failed_login_attempts = 0
        self.locked_until = None
        self.save(update_fields=['failed_login_attempts', 'locked_until'])
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class LoginAttempt(models.Model):
    """Track login attempts for rate limiting"""
    ip_address = models.GenericIPAddressField()
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.email} - {'Success' if self.success else 'Failed'}"


class EmailVerificationToken(models.Model):
    """Store email verification tokens"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} - {'Used' if self.is_used else 'Active'}"


class PasswordResetToken(models.Model):
    """Store password reset tokens"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} - {'Used' if self.is_used else 'Active'}"
    
    def is_expired(self, minutes=15):
        """Check if token is expired"""
        from django.utils import timezone
        from datetime import timedelta
        return timezone.now() - self.created_at > timedelta(minutes=minutes)


# In-memory data store for facts (replace with database models if needed)
FACTS = [
    {
        "id": 1,
        "title": "Python is versatile",
        "content": "Python is a high-level programming language known for its simplicity and versatility.",
        "category": "Programming",
        "tags": ["python", "programming", "language"],
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    },
    {
        "id": 2,
        "title": "Django is powerful",
        "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.",
        "category": "Web Development",
        "tags": ["django", "web", "framework"],
        "created_at": "2024-01-02T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }
]

CATEGORIES = ["Programming", "Web Development", "Science", "History"]

next_id = 3