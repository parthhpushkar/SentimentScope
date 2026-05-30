import React, { useState } from "react";
import axios from "axios";
import "./App.css";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer
} from "recharts";

function App() {
  const [text, setText] = useState("");
  const [prediction, setPrediction] = useState("");
  const [confidence, setConfidence] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [csvFile, setCsvFile] = useState(null);
  const [batchResults, setBatchResults] = useState([]);

  const positiveCount = history.filter(
    item => item.prediction === "Positive"
  ).length;

  const negativeCount = history.filter(
    item => item.prediction === "Negative"
  ).length;

  const chartData = [
    {
      name: "Positive",
      value: positiveCount
    },
    {
      name: "Negative",
      value: negativeCount
    }
  ];

  const COLORS = ["#00E396", "#FF4560"];

  const analyzeSentiment = async () => {
    if (!text.trim()) return;


    setLoading(true);

    try {
      const response = await axios.post(
        "http://localhost:5000/predict",
        {
          text: text,
        }
      );

      setPrediction(response.data.prediction);
      setConfidence(response.data.confidence);

      //history of the analysis 
      setHistory(prev => [
        {
          text,
          prediction: response.data.prediction,
          confidence: response.data.confidence,
          timestamp: new Date().toLocaleTimeString()
        },
        ...prev
      ].slice(0, 10));
    } catch (error) {
      console.log(error);
      alert("Unable to connect to backend");
    }

    setLoading(false);


  };

  //CSV upload function 
  const analyzeCSV = async () => {

    if (!csvFile) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();

    formData.append("file", csvFile);

    try {

      const response = await axios.post(
        "http://localhost:5000/batch_predict",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );

      setBatchResults(response.data);
      console.log("CSV RESPONSE:");
      console.log(response.data);

    } catch (error) {

      console.log(error);

      alert("CSV Analysis Failed");

    }
  };

  return (<div className="app"> <div className="bg-gradient"></div>


    <div className="glass-card">
      <h1 className="title">SentimentScope</h1>

      <p className="subtitle">
        AI Powered Multi-Domain Sentiment Analysis Engine
      </p>

      <textarea
        className="input-box"
        placeholder="Paste a review, tweet, feedback, article, or any text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />


      <div className="csv-section">

        <input
          type="file"
          accept=".csv"
          onChange={(e) =>
            setCsvFile(e.target.files[0])
          }
        />

        <button
          className="csv-btn"
          onClick={() => {
            console.log("CSV BUTTON CLICKED");
            analyzeCSV();
          }}
        >
          Analyze CSV
        </button>

      </div>

      <button
        className="analyze-btn"
        onClick={analyzeSentiment}
        disabled={loading}
      >
        {loading ? (
          <div className="spinner-container">
            <div className="spinner"></div>
            <span>Analyzing...</span>
          </div>
        ) : (
          "Analyze Sentiment"
        )}
      </button>

      {prediction && (
        <div className="result-card">
          <h2>
            {prediction === "Positive" ? "😊 Positive" : "😔 Negative"}
          </h2>

          <p className="confidence-text">
            Confidence: {confidence}%
          </p>

          <div className="progress-container">
            <div
              className="progress-bar"
              style={{ width: `${confidence}%` }}
            ></div>
          </div>
        </div>

      )}
      {history.length > 0 && (
        <div className="history-card">
          <h2>Recent Analyses</h2>

          {history.map((item, index) => (
            <div className="history-item" key={index}>
              <div className="history-header">
                <span>
                  {item.prediction === "Positive"
                    ? "😊 Positive"
                    : "😔 Negative"}
                </span>

                <span>
                  {item.confidence}%
                </span>
              </div>

              <p>{item.text}</p>

              <small>{item.timestamp}</small>
            </div>
          ))}
        </div>
      )}

      {history.length > 0 && (
        <div className="chart-card">

          <h2>Sentiment Analytics</h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >
            <PieChart>
              <Pie
                data={chartData}
                cx="50%"
                cy="50%"
                outerRadius={100}
                dataKey="value"
                label
              >
                {chartData.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={COLORS[index]}
                  />
                ))}
              </Pie>

              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>

        </div>
      )}

      {batchResults.length > 0 && (

        <div className="table-card">

          <h2>Batch Analysis Results</h2>

          <table>

            <thead>

              <tr>
                <th>Review</th>
                <th>Prediction</th>
                <th>Confidence</th>
              </tr>

            </thead>

            <tbody>

              {batchResults.map((item, index) => (

                <tr key={index}>

                  <td>{item.review}</td>

                  <td>
                    {item.prediction === "Positive"
                      ? "😊 Positive"
                      : "😔 Negative"}
                  </td>

                  <td>{item.confidence}%</td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      )}
    </div>

  </div>
  


  );
}

export default App;
