import os
import torch
from batch import batch_predict
import pandas as pd

from flask import Flask, request, jsonify
from flask_cors import CORS

from transformers import (
    BertTokenizer,
    BertForSequenceClassification
)

#flask app

app = Flask(__name__)

CORS(app)

#load model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "../model/saved_model")

tokenizer = BertTokenizer.from_pretrained(model_path)

model = BertForSequenceClassification.from_pretrained(model_path)

model.eval()

#prediction function

def predict_sentiment(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

    logits = outputs.logits

    probabilities = torch.softmax(logits, dim=1)

    confidence, prediction = torch.max(probabilities, dim=1)

    prediction = prediction.item()

    confidence = confidence.item()

    return prediction, confidence

#routes

@app.route("/")
def home():
    return "SentimentScope API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    text = data["text"]

    prediction, confidence = predict_sentiment(text)

    if prediction == 1:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return jsonify({
        "text": text,
        "prediction": sentiment,
        "confidence": round(confidence * 100, 2)
    })

@app.route("/batch_predict", methods=["POST"])
def batch_predict_api():

    if "file" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    file = request.files["file"]

    df = pd.read_csv(file)

    reviews = df["review"].tolist()

    predictions = batch_predict(reviews)

    final_results = []

    for review, result in zip(
        reviews,
        predictions
    ):

        final_results.append({
            "review": review,
            "prediction": result["prediction"],
            "confidence": result["confidence"]
        })

    return jsonify(final_results)
#server runn

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)