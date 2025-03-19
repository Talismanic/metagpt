## config.py

import os

class Config:
    """Configuration class for the Flask application."""
    
    # General settings
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    DEBUG: bool = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
    
    # Database settings
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    
    # Mail settings
    MAIL_SERVER: str = os.environ.get('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT: int = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS: bool = os.environ.get('MAIL_USE_TLS', 'True').lower() in ('true', '1', 't')
    MAIL_USERNAME: str = os.environ.get('MAIL_USERNAME', 'your_email@example.com')
    MAIL_PASSWORD: str = os.environ.get('MAIL_PASSWORD', 'your_email_password')
    MAIL_DEFAULT_SENDER: str = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@example.com')

# Instantiate the configuration
config = Config()
