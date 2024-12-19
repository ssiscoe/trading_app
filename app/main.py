from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database connection
DATABASE = "db/trading_dashboard.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Trading Dashboard API!"})

@app.route("/trends", methods=["GET"])
def get_trends():
    conn = get_db()
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

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO trends (symbol, date, trend_score, predicted_price, actual_price) VALUES (?, ?, ?, ?, ?)",
        (symbol, date, trend_score, predicted_price, actual_price),
    )
    conn.commit()
    return jsonify({"message": "Trend added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
