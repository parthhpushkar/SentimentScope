import os
import torch

from transformers import (
    BertTokenizer,
    BertForSequenceClassification
)

#model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "../model/saved_model")

#tokenizer loading+model

tokenizer = BertTokenizer.from_pretrained(model_path)

model = BertForSequenceClassification.from_pretrained(model_path)

model.eval()

#pridiction function
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

    prediction = torch.argmax(outputs.logits, dim=1).item()

    return prediction

#test

text = "worst movie ever"

result = predict_sentiment(text)

if result == 1:
    print("Positive Sentiment")
else:
    print("Negative Sentiment")