## forms.py

from typing import Optional

class SignupForm:
    """Form for user signup."""
    
    def __init__(self, name: str, email: str, password: str) -> None:
        """Initialize the signup form with user data."""
        self.name: str = name
        self.email: str = email
        self.password: str = password

    def validate(self) -> bool:
        """Validate the signup form data."""
        # Basic validation logic (e.g., check for empty fields)
        return bool(self.name and self.email and self.password)

class LoginForm:
    """Form for user login."""
    
    def __init__(self, email: str, password: str) -> None:
        """Initialize the login form with user credentials."""
        self.email: str = email
        self.password: str = password

    def validate(self) -> bool:
        """Validate the login form data."""
        # Basic validation logic (e.g., check for empty fields)
        return bool(self.email and self.password)
