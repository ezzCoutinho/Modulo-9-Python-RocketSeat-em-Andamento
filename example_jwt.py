from datetime import datetime, timedelta, timezone

import jwt
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            "exp": datetime.now(timezone.utc) + timedelta(minutes=1),
        },
        key="minhaChave",
        algorithm="HS256",
    )
    return jsonify({"token": token}), 200


@app.route("/secret", methods=["POST"])
def secret():
    return jsonify({"message": "my secret"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
