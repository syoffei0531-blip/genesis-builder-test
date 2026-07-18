from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/health/live", methods=["GET"])
def health_live():
    return jsonify({"status": "ok"}), 200


@app.route("/health/ready", methods=["GET"])
def health_ready():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)