from flask import Flask, jsonify, send_from_directory
from app.routes.api import initialize_routes
from app.utils.database import setup_database
from dotenv import load_dotenv
import os

def create_app():
    """
    Application factory to initialize the app with routes and database.
    """
    # Initialize Flask app
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # Application configuration
    app.config["DATABASE"] = os.getenv("DATABASE", "db/trading_dashboard.db")  # Default path if env var not set
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-secret-key")  # Default secret key for development

    # Setup the database
    setup_database(app.config["DATABASE"])  # Create tables from schema.sql if not exists

    # Initialize routes
    initialize_routes(app)  # Add the routes for trends and other features

    # Define favicon route
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            directory='static',
            path='favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )

    # Define a basic index route
    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the Trading Dashboard API!"})

    return app


if __name__ == "__main__":
    # Create and run the app
    app = create_app()
    app.run(debug=True)
