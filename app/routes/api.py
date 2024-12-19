from flask import jsonify, request
import sqlite3

def get_db(app):
    """
    Returns a database connection.
    """
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn

def initialize_routes(app):
    """
    Defines and adds all routes to the Flask app.
    """

    @app.route("/trends", methods=["GET"])
    def get_trends():
        conn = get_db(app)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trends")
        trends = cursor.fetchall()
        return jsonify([dict(trend) for trend in trends])

    @app.route("/add-trend", methods=["POST"])
    def add_trend():
        data = request.json
        symbol = data["symbol"]
        date = data["date"]
        trend_score = data["trend_score"]
        predicted_price = data.get("predicted_price")
        actual_price = data.get("actual_price")

        conn = get_db(app)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO trends (symbol, date, trend_score, predicted_price, actual_price) VALUES (?, ?, ?, ?, ?)",
            (symbol, date, trend_score, predicted_price, actual_price),
        )
        conn.commit()
        return jsonify({"message": "Trend added successfully!"}), 201
