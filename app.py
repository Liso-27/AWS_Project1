# app.py
# Password Strength Analyzer - Web Server
# Run: pip install flask  then  python app.py
# Open browser at: http://localhost:5000

from flask import Flask, request, jsonify, send_from_directory
from analyzer import analyze_password

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    """Serve the main web page"""
    return send_from_directory("static", "index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    API endpoint - receives a password, returns analysis as JSON
    Request:  POST /analyze  with body {"password": "yourpassword"}
    Response: {"score": 7, "strength": "Strong", "checks": {...}, "suggestions": [...]}
    """
    data     = request.get_json()
    password = data.get("password", "")
    result   = analyze_password(password)
    return jsonify(result)


if __name__ == "__main__":
    print("\n  Server running at http://localhost:5000\n")
    app.run(host="0.0.0.0", port=5000)
