from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample training data
texts = [
    "I love this!", "I hate this!", "It is okay.",
    "This is amazing!", "Horrible experience.",
    "I'm happy", "I'm sad", "I feel great", "This sucks", "Mediocre at best"
]
labels = [
    "positive", "negative", "neutral",
    "positive", "negative",
    "positive", "negative", "positive", "negative", "neutral"
]

# Preprocessing and vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Model training
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and vectorizer saved.")
