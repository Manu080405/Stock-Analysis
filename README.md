# 📈 Stock Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20CSS%20JS-orange)
![API](https://img.shields.io/badge/API-yFinance-green)
![License](https://img.shields.io/badge/License-MIT-red)

An **interactive stock analysis dashboard** that allows users to analyze historical stock data using **Yahoo Finance API**.

The project provides a **modern animated web interface** to retrieve and visualize stock price data for selected tickers within a given date range.

---

# 🚀 Features

## 📊 Stock Data Retrieval
- Fetch historical stock data using **yFinance**
- Supports **multiple stock tickers**
- Select **custom date range**

## 💻 Interactive Dashboard
- Modern UI with **glassmorphism design**
- Animated interface
- Responsive layout

## ⚡ Fast Backend
- Built with **Flask**
- API endpoint to fetch stock data
- JSON-based communication

## 📈 Data Display
Stock data table includes:

- Open price  
- High price  
- Low price  
- Close price  
- Volume  

## 🎨 UI Enhancements
- Loading animation
- Hover effects
- Dashboard cards
- Statistics counters

---

# 🖥️ Demo Interface

## Dashboard
Users can enter stock tickers and select a date range.

Example input:

```
TSLA, AMZN, AMD
```

## Data Output

| Date | Open | High | Low | Close | Volume |
|-----|-----|-----|-----|-----|-----|

---

# 🏗️ Project Architecture

```
Stock-Analysis
│
├── app.py              # Flask backend server
├── Stock.py            # Stock data retrieval logic
│
├── templates
│   └── index.html      # Frontend page
│
└── static
    ├── style.css       # Styling and animations
    └── script.js       # API requests and DOM updates
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/Manu080405/Stock-Analysis.git
```

```
cd Stock-Analysis
```

---

## 2️⃣ Install Dependencies

```
pip install flask yfinance pandas
```

---

## 3️⃣ Run the Application

```
python app.py
```

---

## 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

# 🧠 How It Works

### Step 1
User enters:
- Stock tickers
- Start date
- End date

### Step 2
Frontend sends request

```
POST /get_stock
```

### Step 3
Flask backend calls

```
yfinance.download()
```

### Step 4
Data returned as JSON

### Step 5
Frontend renders results in table

---

# 🔌 API Endpoint

## POST `/get_stock`

### Request

```json
{
  "tickers": ["TSLA","AMZN"],
  "start_date": "2024-01-01",
  "end_date": "2024-02-01"
}
```

### Response

```json
[
  {
    "Date": "2024-01-01",
    "Open": 230.5,
    "High": 235.1,
    "Low": 228.4,
    "Close": 233.9,
    "Volume": 34000000
  }
]
```

---

# 🎯 Future Improvements

- 📈 Interactive **stock charts**
- 📊 Candlestick visualization
- 📉 Moving average indicators
- ⚡ Real-time stock price updates
- 🤖 AI-based stock prediction
- 📊 Portfolio tracking

---

# 🧑‍💻 Tech Stack

## Backend
- Python
- Flask

## Data API
- yFinance

## Frontend
- HTML
- CSS
- JavaScript

## Visualization (Future)
- Chart.js
- Plotly

---

# 📚 Learning Outcomes

This project demonstrates:

- REST API development
- Backend–Frontend integration
- Financial data processing
- Interactive UI design
- Flask application architecture

---
