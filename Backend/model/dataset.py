from datasets import load_dataset
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset from Hugging Face
dataset = load_dataset("dipanjanS/imdb_sentiment_finetune_dataset20k")

df = dataset["train"].to_pandas()   
print(dataset)
print(df.head())
print(df.columns)
print(df.shape)
print(df.isnull().sum())
df = df.dropna()
print(df["label"].value_counts())

train_texts, val_texts, train_labels, val_labels = train_test_split(
    df["text"],
    df["label"],
    test_size=0.2,
    random_state=42
)