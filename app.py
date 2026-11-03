
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Python application deployed successfully!",
        "environment": "AWS Private EC2",
        "status": "Running",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
