"""
Email service for sending transactional emails
Supports SendGrid and AWS SES
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


def send_email_verification_email(user, token):
    """Send email verification email to user"""
    verification_url = f"{settings.FRONTEND_URL}/verify-email/{token}"
    
    subject = "Verify Your Email - Facts Hub"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background-color: #4F46E5; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background-color: #f9f9f9; }}
            .button {{ 
                display: inline-block; 
                padding: 12px 24px; 
                background-color: #4F46E5; 
                color: white; 
                text-decoration: none; 
                border-radius: 6px;
                margin: 20px 0;
            }}
            .footer {{ text-align: center; padding: 20px; font-size: 12px; color: #666; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Facts Hub</h1>
            </div>
            <div class="content">
                <h2>Welcome, {user.username}!</h2>
                <p>Thank you for registering with Facts Hub. Please verify your email address by clicking the button below:</p>
                <p style="text-align: center;">
                    <a href="{verification_url}" class="button">Verify Email Address</a>
                </p>
                <p>If the button doesn't work, copy and paste this link into your browser:</p>
                <p>{verification_url}</p>
                <p>This link will expire in 24 hours.</p>
                <p>If you didn't create an account, please ignore this email.</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Facts Hub. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    text_content = f"""
    Welcome, {user.username}!
    
    Thank you for registering with Facts Hub. Please verify your email address by visiting:
    {verification_url}
    
    This link will expire in 24 hours.
    
    If you didn't create an account, please ignore this email.
    
    -- Facts Hub Team
    """
    
    return send_email(
        to_email=user.email,
        subject=subject,
        html_content=html_content,
        text_content=text_content
    )


def send_password_reset_email(user, token):
    """Send password reset email to user"""
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{token}"
    
    subject = "Password Reset Request - Facts Hub"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background-color: #4F46E5; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background-color: #f9f9f9; }}
            .button {{ 
                display: inline-block; 
                padding: 12px 24px; 
                background-color: #EF4444; 
                color: white; 
                text-decoration: none; 
                border-radius: 6px;
                margin: 20px 0;
            }}
            .warning {{ 
                background-color: #FEF3C7; 
                border-left: 4px solid #F59E0B; 
                padding: 12px; 
                margin: 16px 0;
                font-size: 14px;
            }}
            .footer {{ text-align: center; padding: 20px; font-size: 12px; color: #666; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Facts Hub</h1>
            </div>
            <div class="content">
                <h2>Password Reset Request</h2>
                <p>We received a request to reset your password. Click the button below to reset it:</p>
                <p style="text-align: center;">
                    <a href="{reset_url}" class="button">Reset Password</a>
                </p>
                <p>If the button doesn't work, copy and paste this link into your browser:</p>
                <p>{reset_url}</p>
                <div class="warning">
                    <strong>Important:</strong> This link expires in 15 minutes for your security.
                </div>
                <p>If you didn't request a password reset, please ignore this email or contact support if you have concerns.</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Facts Hub. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    text_content = f"""
    Password Reset Request
    
    We received a request to reset your password. Visit the following link to reset it:
    {reset_url}
    
    Important: This link expires in 15 minutes for your security.
    
    If you didn't request a password reset, please ignore this email or contact support.
    
    -- Facts Hub Team
    """
    
    return send_email(
        to_email=user.email,
        subject=subject,
        html_content=html_content,
        text_content=text_content
    )


def send_welcome_email(user):
    """Send welcome email after email verification"""
    subject = "Welcome to Facts Hub!"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background-color: #4F46E5; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; background-color: #f9f9f9; }}
            .button {{ 
                display: inline-block; 
                padding: 12px 24px; 
                background-color: #4F46E5; 
                color: white; 
                text-decoration: none; 
                border-radius: 6px;
                margin: 20px 0;
            }}
            .footer {{ text-align: center; padding: 20px; font-size: 12px; color: #666; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Facts Hub</h1>
            </div>
            <div class="content">
                <h2>Welcome, {user.username}!</h2>
                <p>Your email has been verified successfully. You're now a full member of Facts Hub!</p>
                <p style="text-align: center;">
                    <a href="{settings.FRONTEND_URL}/dashboard" class="button">Go to Dashboard</a>
                </p>
                <p>Explore interesting facts, add your own, and enjoy learning something new every day.</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Facts Hub. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    text_content = f"""
    Welcome to Facts Hub, {user.username}!
    
    Your email has been verified successfully. You're now a full member of Facts Hub!
    
    Visit your dashboard: {settings.FRONTEND_URL}/dashboard
    
    -- Facts Hub Team
    """
    
    return send_email(
        to_email=user.email,
        subject=subject,
        html_content=html_content,
        text_content=text_content
    )


def send_email(to_email, subject, html_content, text_content):
    """
    Send email using configured email provider
    Returns True if email was sent successfully, False otherwise
    """
    try:
        if settings.EMAIL_PROVIDER == 'sendgrid':
            return send_via_sendgrid(to_email, subject, html_content, text_content)
        else:
            # Use Django's default email backend
            return send_via_smtp(to_email, subject, html_content, text_content)
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {str(e)}")
        return False


def send_via_sendgrid(to_email, subject, html_content, text_content):
    """Send email via SendGrid API"""
    try:
        import sendgrid
        from sendgrid.helpers.mail import Mail, Email, To, Content
        
        sg = sendgrid.SendGridAPIClient(api_key=settings.EMAIL_API_KEY)
        
        from_email = Email(settings.EMAIL_FROM)
        to_email = To(to_email)
        
        content = Content("text/html", html_content)
        
        mail = Mail(from_email, to_email, subject, content)
        mail.personalizations[0].add_content(Content("text/plain", text_content))
        
        response = sg.send(mail)
        
        if response.status_code in [200, 202]:
            logger.info(f"Email sent successfully to {to_email} via SendGrid")
            return True
        else:
            logger.error(f"SendGrid API error: {response.status_code} - {response.body}")
            return False
            
    except ImportError:
        logger.warning("SendGrid not installed, falling back to SMTP")
        return send_via_smtp(to_email, subject, html_content, text_content)
    except Exception as e:
        logger.error(f"SendGrid error: {str(e)}")
        return False


def send_via_smtp(to_email, subject, html_content, text_content):
    """Send email via SMTP"""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = settings.EMAIL_FROM
        msg['To'] = to_email
        
        part1 = MIMEText(text_content, 'plain')
        part2 = MIMEText(html_content, 'html')
        
        msg.attach(part1)
        msg.attach(part2)
        
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            if settings.EMAIL_API_KEY:
                server.login(settings.EMAIL_FROM, settings.EMAIL_API_KEY)
            server.sendmail(settings.EMAIL_FROM, to_email, msg.as_string())
        
        logger.info(f"Email sent successfully to {to_email} via SMTP")
        return True
        
    except Exception as e:
        logger.error(f"SMTP error: {str(e)}")
        return False