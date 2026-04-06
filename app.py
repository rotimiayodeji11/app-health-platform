import logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home endpoint called")
    return "Hello DevOps 🚀"

@app.route("/health")
def health():
    app.logger.info("Health check called")
    return jsonify({"status": "healthy"})

@app.route("/ready")
def ready():
    app.logger.info("Readiness check called")
    return jsonify({"status": "ready"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)