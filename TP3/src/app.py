from flask import Flask, jsonify
from datetime import datetime
import logging
import os

# Création du dossier logs
os.makedirs("/app/logs", exist_ok=True)

# On écrit dans /app/logs
logging.basicConfig(
    filename="/app/logs/log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Route appelée")
    return jsonify({
        "message": "API Flask opérationnelle",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)