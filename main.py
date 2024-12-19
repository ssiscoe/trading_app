from flask import Flask, jsonify
from app.routes.api import initialize_routes
from app.utils.database import setup_database
from dotenv import load_dotenv
import os

# Initialize Flask app
app = Flask(__name__)

# Database path
app.config["DATABASE"] = "db/trading_dashboard.db"

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Trading Dashboard API!"})

def create_app():
    """
    Application factory to initialize the app with routes and database.
    """
    # Step 1: Setup the database
    setup_database(app.config["DATABASE"])  # Create tables from schema.sql if not exists

    # Step 2: Initialize routes
    initialize_routes(app)  # Add the routes for trends and other features

    load_dotenv()  # Load environment variables from .env file
    app.config['DATABASE'] = os.getenv('DATABASE')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    return app

if __name__ == "__main__":
    # Create and run the app
    app = create_app()
    app.run(debug=True)
