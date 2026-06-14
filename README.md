<h1 align="center">🏏 IPL Win Probability Predictor</h1>

<p align="center">
  <b>A Machine Learning powered IPL Win Probability Prediction API built with FastAPI & Scikit-learn.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy">
</p>

---

# 📌 Overview

IPL Win Probability Predictor is an AI-powered Machine Learning application that predicts the probability of a team winning an IPL match based on real-time match conditions.

The project exposes a REST API using FastAPI, making it easy to integrate with web applications or dashboards.

---

# 🚀 Features

✅ Machine Learning Prediction

✅ FastAPI REST API

✅ Data Preprocessing Pipeline

✅ Scikit-learn Model

✅ Input Validation using Pydantic

✅ Swagger Documentation

✅ Ready for Deployment

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | Backend API |
| Scikit-learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Pickle | Model Serialization |

---

# 📂 Project Structure

```
IPL-Win-Probability-Predictor
│
├── main.py
├── ipl_model.pkl
├── ipl_transformer.pkl
├── requirements.txt
├── README.md
└── deliveries.csv
|__matches.csv
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/IPL-Win-Probability-Predictor.git
```

Go to project directory

```bash
cd IPL-Win-Probability-Predictor
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run API

```bash
uvicorn main:app --reload
```

---

# 📡 API Endpoint

POST

```
/predict
```

Sample Input

```json
{
  "batting_team":"Mumbai Indians",
  "bowling_team":"Chennai Super Kings",
  "city":"Mumbai",
  "runs_left":80,
  "balls_left":60,
  "wickets":6,
  "total_runs_x":180
}
```

Sample Response

```json
{
   "Win Probability":82.63,
   "Lose Probability":17.37
}
```

---

# 📈 Machine Learning Workflow

Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

Preprocessing

↓

Model Training

↓

Prediction API

---

# 📖 API Documentation

FastAPI automatically provides Swagger UI.

```
http://127.0.0.1:8000/docs
```

---

# 📌 Future Improvements

- Streamlit Dashboard
- React Frontend
- Docker Support
- Cloud Deployment
- Live IPL Data Integration
- User Authentication

---

# 👩‍💻 Author

### Anushka Singh

AI | Machine Learning | FastAPI | Generative AI

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://linkedin.com/in/YOUR_PROFILE

---

<h3 align="center">
⭐ If you like this project, don't forget to Star the Repository ⭐
</h3>
