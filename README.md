# Crypto Tracker Platform

A dynamic cryptocurrency tracking dashboard built with Python (Flask) and JavaScript (Chart.js). This application fetches real-time market data using the free CoinGecko API and presents it in a sleek, responsive, Dark Mode-themed UI using Bootstrap 5.

## 🚀 Features

- **Live Market Data:** View the top 50 cryptocurrencies ranked by market capitalization.
- **Dynamic Styling:** Price changes over the last 24 hours are automatically color-coded (green for profit, red for loss).
- **Search Functionality:** Instantly filter coins by name or symbol (e.g., BTC, Ethereum).
- **Detailed Coin Profiles:** View comprehensive statistics including Market Cap, 24h Volume, Circulating Supply, ATH, and ATL.
- **Interactive Price Charts:** Historical 7-day price data is dynamically fetched and visualized using **Chart.js** for an interactive line chart experience with tooltips.
- **API Caching:** Built-in memory caching mechanism to prevent hitting API rate limits during rapid page reloads.

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask, `requests`
- **Frontend:** HTML5, CSS3, Jinja2, Bootstrap 5, Chart.js
- **External API:** [CoinGecko API v3](https://www.coingecko.com/en/api) (No API Key Required)

## 📦 Setup & Installation Guide

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crypto-tracker.git
cd crypto-tracker
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Since this project uses the public CoinGecko API, there is no need to configure any environment variables (`.env`). It works right out of the box!

```bash
flask run
```

The application will start on `http://127.0.0.1:5000`. Open this URL in your browser to view the live dashboard!
