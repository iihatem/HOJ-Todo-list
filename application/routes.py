from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
import boto3
from application import cognito_client, USER_POOL_ID, CLIENT_ID, app
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

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

            # Simulating the login with Flask-Login
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

# Task Management Routes (CRUD)
# Route to create a new task
@main.route('/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    task = {
        'title': data['title'],
        'description': data['description'],
        'status': 'Pending',
        'owner': current_user.get_id(),
    }
    app.db.tasks.insert_one(task)
    return jsonify({'message': 'Task created successfully'}), 201

# Route to fetch all tasks
@main.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
    tasks = list(app.db.tasks.find({'owner': current_user.get_id()}))
    for task in tasks:
        task['_id'] = str(task['_id'])  # Convert ObjectId to string for JSON
    return jsonify(tasks), 200

# Route to update a task
@main.route('/tasks/<task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    result = app.db.tasks.update_one(
        {'_id': ObjectId(task_id), 'owner': current_user.get_id()},
        {'$set': {'status': data['status']}}
    )

    if result.matched_count == 0:
        return jsonify({'error': 'Task not found or unauthorized'}), 404

    return jsonify({'message': 'Task updated successfully'}), 200

# Route to delete a task
@main.route('/tasks/<task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    result = app.db.tasks.delete_one(
        {'_id': ObjectId(task_id), 'owner': current_user.get_id()}
    )

    if result.deleted_count == 0:
        return jsonify({'error': 'Task not found or unauthorized'}), 404

    return jsonify({'message': 'Task deleted successfully'}), 200
