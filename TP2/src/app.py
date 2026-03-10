from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur l'API Flask"

@app.route("/api/status")
def status():
    return jsonify({"status": "OK"})

@app.route("/api/user/<name>")
def user(name):
    return jsonify({
        "name": name,
        "role": "student"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)