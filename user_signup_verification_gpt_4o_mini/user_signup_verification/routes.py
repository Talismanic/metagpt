## routes.py

from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from models import UserManager, User
from forms import SignupForm, LoginForm
from config import config

# Initialize Flask app and mail
app = Flask(__name__)
app.config.from_object(config)
mail = Mail(app)

@app.route('/signup', methods=['POST'])
def signup():
    """Handle user signup."""
    data = request.get_json()
    form = SignupForm(name=data.get('name'), email=data.get('email'), password=data.get('password'))

    if form.validate():
        if UserManager.create_user(form.name, form.email, form.password):
            user = User.query.filter_by(email=form.email).first()
            UserManager.send_verification_email(user)
            return jsonify({"message": "User created successfully"}), 200
        return jsonify({"error": "Email already exists"}), 400
    
    return jsonify({"error": "Invalid input"}), 400

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.get_json()
    form = LoginForm(email=data.get('email'), password=data.get('password'))

    if form.validate():
        user = User.query.filter_by(email=form.email).first()
        if user and user.check_password(form.password):
            if user.is_active:
                return jsonify({"message": "Login successful"}), 200
            return jsonify({"error": "Account not activated"}), 401
        
        return jsonify({"error": "Invalid credentials"}), 401
    
    return jsonify({"error": "Invalid input"}), 400

@app.route('/verify/<email>', methods=['GET'])
def verify(email: str):
    """Activate user account."""
    UserManager.activate_user(email)
    flash('Your account has been activated!', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
