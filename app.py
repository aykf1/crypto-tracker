import time
from datetime import datetime
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BASE_URL = "https://api.coingecko.com/api/v3"

# Simple memory cache to avoid hitting CoinGecko API rate limits (Free tier is very strict)
cache = {
    "markets": {"data": None, "timestamp": 0},
}
CACHE_DURATION = 60  # Cache duration in seconds (1 minute)

def get_market_data():
    """Fetch top 50 cryptocurrencies with caching."""
    current_time = time.time()
    
    # Return cached data if valid
    if cache["markets"]["data"] and (current_time - cache["markets"]["timestamp"] < CACHE_DURATION):
        return cache["markets"]["data"], None
        
    url = f"{BASE_URL}/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 429:
            return cache["markets"]["data"] or [], "Çok fazla istek yapıldı. API limiti aşıldı, lütfen 1 dakika bekleyin."
            
        response.raise_for_status()
        data = response.json()
        
        # Update cache
        cache["markets"]["data"] = data
        cache["markets"]["timestamp"] = current_time
        return data, None
        
    except requests.RequestException as e:
        print(f"Error fetching market data: {e}")
        # Return old cache if available, else empty list
        return cache["markets"]["data"] or [], "Veriler çekilirken bir bağlantı hatası oluştu."

@app.route("/")
def index():
    """Home page: Lists top cryptocurrencies."""
    coins, error = get_market_data()
    return render_template("index.html", coins=coins, error=error)

@app.route("/search")
def search():
    """Search for a specific coin locally from the cached top 50 list to save API calls."""
    query = request.args.get("q", "").strip().lower()
    if not query:
        return redirect(url_for("index"))
        
    coins, error = get_market_data()
    
    # Filter coins by name or symbol locally
    filtered_coins = [
        c for c in coins 
        if query in c.get("name", "").lower() or query in c.get("symbol", "").lower()
    ]
    
    return render_template("index.html", coins=filtered_coins, error=error, query=query)

@app.route("/coin/<string:coin_id>")
def coin_detail(coin_id):
    """Show detailed information for a specific coin."""
    # 1. Fetch basic details
    detail_url = f"{BASE_URL}/coins/{coin_id}"
    detail_params = {
        "localization": "false",
        "tickers": "false",
        "market_data": "true",
        "community_data": "false",
        "developer_data": "false",
        "sparkline": "false"
    }
    
    # 2. Fetch 7-day chart data
    chart_url = f"{BASE_URL}/coins/{coin_id}/market_chart"
    chart_params = {
        "vs_currency": "usd",
        "days": "7"
    }
    
    try:
        # Get details
        resp_detail = requests.get(detail_url, params=detail_params, timeout=10)
        if resp_detail.status_code == 429:
            return render_template("coin_detail.html", error="API Limiti Aşıldı. Lütfen biraz bekleyip sayfayı yenileyin.")
        resp_detail.raise_for_status()
        coin_data = resp_detail.json()
        
        # Get chart data
        chart_labels = []
        chart_data = []
        try:
            resp_chart = requests.get(chart_url, params=chart_params, timeout=10)
            if resp_chart.status_code == 200:
                prices = resp_chart.json().get("prices", [])
                for p in prices:
                    # p[0] is timestamp in ms, p[1] is price
                    timestamp = p[0] / 1000.0
                    dt = datetime.fromtimestamp(timestamp)
                    chart_labels.append(dt.strftime("%d %b")) # e.g. "08 Aug"
                    chart_data.append(p[1])
        except Exception as e:
            print(f"Error fetching chart data: {e}")
            
        return render_template("coin_detail.html", coin=coin_data, chart_labels=chart_labels, chart_data=chart_data)
        
    except requests.RequestException as e:
        print(f"Error fetching coin details: {e}")
        return render_template("coin_detail.html", error="Coin detayları yüklenirken bir hata oluştu.")

# Custom template filter for formatting currency
@app.template_filter('currency')
def currency_format(value):
    if value is None:
        return "$0.00"
    if value >= 1000000000:
        return f"${value / 1000000000:.2f} Milyar"
    if value >= 1000000:
        return f"${value / 1000000:.2f} Milyon"
    if value < 0.01:
        return f"${value:.6f}"
    return f"${value:,.2f}"

if __name__ == "__main__":
    app.run(debug=True)
