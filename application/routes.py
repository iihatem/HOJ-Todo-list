from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
import boto3
from application import cognito_client, USER_POOL_ID, CLIENT_ID
from werkzeug.security import generate_password_hash, check_password_hash

# Define the Blueprint
main = Blueprint('main', __name__)

# Route to display home page (public route)
@main.route('/')
def home():
    return "Welcome to the To-Do List App"

# Route to handle sign-up (creating a new user)
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('main.signup'))

        try:
            # Create the user in AWS Cognito (this assumes your Cognito user pool is configured with email as username)
            response = cognito_client.sign_up(
                ClientId=CLIENT_ID,
                Username=email,
                Password=password,
                UserAttributes=[
                    {'Name': 'email', 'Value': email},
                    {'Name': 'preferred_username', 'Value': username}
                ]
            )
            flash('Sign up successful! Please check your email to verify your account.', 'success')
            return redirect(url_for('main.signin'))
        except cognito_client.exceptions.UsernameExistsException:
            flash('Username already exists. Please choose another one.', 'danger')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
    
    return render_template('signup.html')

# Route to handle sign-in (log in existing user)
@main.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            # Call AWS Cognito to authenticate user
            response = cognito_client.initiate_auth(
                ClientId=CLIENT_ID,
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={'USERNAME': email, 'PASSWORD': password}
            )

            # Assuming successful login, set the user ID (or some token) for Flask-Login session
            session_token = response['AuthenticationResult']['IdToken']

            # Ideally, you would save the token or user info to track the session in Flask
            # For now, we simulate the login with Flask-Login
            login_user(current_user)  # Assuming we have a valid current_user

            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.home'))
        except cognito_client.exceptions.NotAuthorizedException:
            flash('Incorrect username or password. Please try again.', 'danger')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')
    
    return render_template('signin.html')

# Route to handle sign-out (log out user)
@main.route('/signout')
@login_required
def signout():
    logout_user()
    flash('You have logged out successfully.', 'success')
    return redirect(url_for('main.home'))

# Route to manage profile (optional, could be for updating user details)
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

