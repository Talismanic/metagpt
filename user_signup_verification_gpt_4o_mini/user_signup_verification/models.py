## models.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize the database and bcrypt
db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    """User model for storing user information."""
    
    __tablename__ = 'users'
    
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(128), nullable=False)
    is_active: bool = db.Column(db.Boolean, default=False)

    def __init__(self, name: str, email: str, password: str) -> None:
        """Initialize a new user with name, email, and password."""
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password: str) -> None:
        """Set the user's password hash."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        """Check if the provided password matches the stored password hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

class UserManager:
    """User management class for handling user-related operations."""
    
    @staticmethod
    def create_user(name: str, email: str, password: str) -> bool:
        """Create a new user if the email is unique."""
        if UserManager.is_email_unique(email):
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return True
        return False

    @staticmethod
    def is_email_unique(email: str) -> bool:
        """Check if the provided email is unique in the database."""
        return User.query.filter_by(email=email).first() is None

    @staticmethod
    def send_verification_email(user: User) -> None:
        """Send a verification email to the user."""
        # Implementation for sending email will be done in routes.py
        pass

    @staticmethod
    def activate_user(email: str) -> None:
        """Activate the user account based on the email."""
        user = User.query.filter_by(email=email).first()
        if user:
            user.is_active = True
            db.session.commit()

class SignupForm:
    """Form for user signup."""
    
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

    def validate(self) -> bool:
        """Validate the signup form data."""
        # Basic validation logic (e.g., check for empty fields)
        return bool(self.name and self.email and self.password)

class LoginForm:
    """Form for user login."""
    
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def validate(self) -> bool:
        """Validate the login form data."""
        # Basic validation logic (e.g., check for empty fields)
        return bool(self.email and self.password)
