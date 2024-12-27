from flask import Flask
from flask_login import LoginManager
import boto3

# Initialize Flask app
app = Flask(__name__)

# Set secret key for session management
app.config['SECRET_KEY'] = 'Omar_sucks'  # Change this to a secure key in production

# Initialize AWS Cognito client (replace 'your-region' with the correct region for your User Pool)
cognito_client = boto3.client('cognito-idp', region_name='your-region')

# Cognito details - replace with your User Pool and App Client ID
USER_POOL_ID = 'your-user-pool-id'
CLIENT_ID = 'your-app-client-id'

# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create the user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # You can expand this to load user details from the database or Cognito
    # Here, we assume `user_id` is an email address for simplicity
    return User(user_id)

# Import routes after app is created (to avoid circular imports)
from application.routes import main

def create_app():
    # Register Blueprints (you can have multiple blueprints for larger applications)
    app.register_blueprint(main)

    return app

