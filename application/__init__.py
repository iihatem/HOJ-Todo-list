from flask import Flask
from flask_pymongo import PyMongo

# Initialize MongoDB
mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Application configurations
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo_app'

    # Initialize MongoDB
    mongo.init_app(app)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app

