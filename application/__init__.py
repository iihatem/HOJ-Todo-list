from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration (Can be added later)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Used for session management

    # Import routes
    from application.routes import main
    app.register_blueprint(main)

    return app


