# backend/app/main.py

from flask import Flask, request, jsonify
from app.model import predict_sentiment
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction = predict_sentiment(text)
    return jsonify({"sentiment": prediction})

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Sentiment API with Hugging Face is running."})
