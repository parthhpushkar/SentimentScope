import os
import torch

from transformers import (
    BertTokenizer,
    BertForSequenceClassification
)

#mode loading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "../model/saved_model"
)

tokenizer = BertTokenizer.from_pretrained(model_path)

model = BertForSequenceClassification.from_pretrained(
    model_path
)

model.eval()

#batch prediction function

def batch_predict(texts):

    inputs = tokenizer(
        texts,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

    probabilities = torch.softmax(
        outputs.logits,
        dim=1
    )

    predictions = torch.argmax(
        outputs.logits,
        dim=1
    )

    results = []

    for i, pred in enumerate(predictions):

        sentiment = (
            "Positive"
            if pred.item() == 1
            else "Negative"
        )

        confidence = round(
            probabilities[i][pred].item() * 100,
            2
        )

        results.append({
            "prediction": sentiment,
            "confidence": confidence
        })

    return results