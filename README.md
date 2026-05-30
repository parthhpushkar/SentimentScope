# 🚀 SentimentScope

AI-Powered Multi-Domain Sentiment Analysis Platform built using **BERT, PyTorch, Flask, React, Docker, and Hugging Face**.

## 📌 Overview

SentimentScope is an end-to-end AI application that analyzes the sentiment of user-provided text and classifies it as **Positive** or **Negative** using a fine-tuned BERT model.

The platform supports:

* Real-time sentiment prediction
* Batch CSV sentiment analysis
* Confidence score visualization
* Sentiment history tracking
* Analytics dashboard with charts
* Live AI model deployment using Hugging Face Spaces

---

## 🌐 Live Demo

### Hugging Face Demo

https://huggingface.co/spaces/parthhpushkar/sentimentscope

### Model Repository

https://huggingface.co/parthhpushkar/sentimentscope-bert

### GitHub Repository

https://github.com/parthhpushkar/SentimentScope

---

## ✨ Features

### 🔹 Real-Time Sentiment Analysis

Analyze user reviews, tweets, feedback, and text instantly.

### 🔹 Confidence Score

Displays model confidence for every prediction.

### 🔹 Batch CSV Analysis

Upload CSV files containing reviews and get predictions for multiple records simultaneously.

### 🔹 Sentiment History

Tracks previously analyzed texts and their sentiment results.

### 🔹 Analytics Dashboard

Interactive sentiment distribution visualization using pie charts.

### 🔹 Modern UI

Dark theme glassmorphism interface built with React.

### 🔹 Dockerized Deployment

Frontend and backend containerized using Docker and Docker Compose.

---

## 🏗️ System Architecture

User Input / CSV Upload

↓

React Frontend

↓

Flask REST API

↓

Fine-Tuned BERT Model

↓

Prediction + Confidence Score

↓

Analytics Dashboard

---

## 🛠️ Tech Stack

### AI / Machine Learning

* Python
* PyTorch
* Hugging Face Transformers
* BERT
* Safetensors

### Backend

* Flask
* Flask-CORS
* Pandas

### Frontend

* React.js
* Axios
* Recharts

### DevOps

* Docker
* Docker Compose
* GitHub

### Deployment

* Hugging Face Hub
* Hugging Face Spaces
* Vercel

---

## 📊 Model Details

Model Architecture:

* BERT For Sequence Classification

Task:

* Binary Sentiment Classification

Classes:

* Positive
* Negative

Deployment Model:

* Hosted on Hugging Face Hub

---

## 📁 Project Structure

SentimentScope/

├── Backend/

│ ├── api/

│ ├── model/

│ └── requirements.txt

│

├── frontend/

│ ├── src/

│ ├── public/

│ └── package.json

│

├── docker-compose.yml

└── README.md

---

## 🚀 Local Setup

### Backend

```bash
pip install -r requirements.txt

python api/app.py
```

### Frontend

```bash
npm install

npm start
```

### Docker

```bash
docker-compose up --build
```

---

## 📸 Screenshots





## 👨‍💻 Author

Parth Pushkar

LinkedIn: Add Your LinkedIn Profile

GitHub: https://github.com/parthhpushkar
