from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "SpamShield AI Backend is running 🚀"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    message = data.get("message", "")

    if not message:
        return jsonify({
            "error": "Message is required"
        }), 400

    # Temporary detection logic.
    # We will replace this with our ML model later.

    suspicious_words = [
        "winner",
        "won",
        "prize",
        "free",
        "urgent",
        "claim",
        "click",
        "money",
        "cash",
        "lottery",
        "verify",
        "password"
    ]

    message_lower = message.lower()

    detected_words = [
        word for word in suspicious_words
        if word in message_lower
    ]

    if len(detected_words) >= 2:

        prediction = "Spam"
        probability = min(
            95,
            60 + len(detected_words) * 7
        )

    else:

        prediction = "Not Spam"
        probability = max(
            5,
            len(detected_words) * 10
        )

    return jsonify({
        "prediction": prediction,
        "probability": probability,
        "detected_words": detected_words
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
