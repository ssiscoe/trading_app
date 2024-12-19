from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/trades", methods=["GET", "POST"])
def manage_trades():
    if request.method == "GET":
        return jsonify({"message": "Fetching trades..."})
    elif request.method == "POST":
        data = request.json
        return jsonify({"message": "Trade executed", "trade": data})

def initialize_routes():
    app.run(debug=True)
