from datasets import load_dataset
import pandas as pd
import torch

from sklearn.model_selection import train_test_split

from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments
)

#dataset loads 

dataset = load_dataset("dipanjanS/imdb_sentiment_finetune_dataset20k")

df = dataset["train"].to_pandas()

print(df.head())

#null value removed 

df = df.dropna()

#training of split data

train_texts, val_texts, train_labels, val_labels = train_test_split(
    df["review"],
    df["sentiment"],
    test_size=0.2,
    random_state=42
)

#tokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

train_encodings = tokenizer(
    train_texts.tolist(),
    truncation=True,
    padding=True,
    max_length=128
)

val_encodings = tokenizer(
    val_texts.tolist(),
    truncation=True,
    padding=True,
    max_length=128
)

#dataset class

class SentimentDataset(torch.utils.data.Dataset):

    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels.tolist()

    def __getitem__(self, idx):

        item = {
            key: torch.tensor(val[idx])
            for key, val in self.encodings.items()
        }

        item["labels"] = torch.tensor(self.labels[idx])

        return item

    def __len__(self):
        return len(self.labels)


train_dataset = SentimentDataset(train_encodings, train_labels)

val_dataset = SentimentDataset(val_encodings, val_labels)

#bert model loads 

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)

#training arguments 

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=8,
    logging_dir="./logs"
)

#trainer 

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

#training starts 

trainer.train()

#models being saved 

model.save_pretrained("./saved_model")

tokenizer.save_pretrained("./saved_model")

print("MODEL SAVED SUCCESSFULLY")