# backend/app/model.py

from transformers import pipeline

# Load pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

def predict_sentiment(text: str) -> str:
    """Use Hugging Face model to classify sentiment."""
    result = classifier(text)[0]
    label = result["label"].lower()  # returns 'POSITIVE' or 'NEGATIVE'
    return label
