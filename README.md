# Kripto Para Takip Platformu

[English](#crypto-tracker-platform) | [Türkçe](#kripto-para-takip-platformu)

## Türkçe

Python (Flask) ve JavaScript (Chart.js) ile geliştirilmiş dinamik bir kripto para takip paneli. Ücretsiz CoinGecko API’sinden piyasa verilerini alır ve Bootstrap 5 ile hazırlanmış, duyarlı ve koyu temalı bir arayüzde sunar.

### Özellikler

- **Canlı piyasa verileri:** Piyasa değerine göre sıralanmış en büyük 50 kripto parayı görüntüleme.
- **Dinamik renklendirme:** Son 24 saatteki fiyat değişimlerini yeşil (artış) veya kırmızı (düşüş) renkte gösterme.
- **Arama:** Coin’leri adına veya sembolüne göre anında filtreleme (ör. BTC, Ethereum).
- **Coin detayları:** Piyasa değeri, 24 saatlik işlem hacmi, dolaşımdaki arz, tüm zamanların en yüksek ve en düşük fiyatı gibi istatistikleri görüntüleme.
- **Etkileşimli fiyat grafikleri:** Son 7 günlük fiyat verilerini Chart.js ile çizgi grafik olarak görüntüleme.
- **API önbelleği:** Sayfa sık yenilendiğinde API isteklerini azaltmaya yardımcı olan bellek içi önbellek.

### Kullanılan Teknolojiler

- **Arka uç:** Python 3, Flask, `requests`
- **Ön yüz:** HTML5, CSS3, Jinja2, Bootstrap 5, Chart.js
- **Harici API:** [CoinGecko API v3](https://www.coingecko.com/en/api) (API anahtarı gerekmez)

### Kurulum ve Çalıştırma

Uygulamayı bilgisayarında çalıştırmak için:

1. Depoyu klonla:

   ```bash
   git clone https://github.com/yourusername/crypto-tracker.git
   cd crypto-tracker
   ```

2. Sanal ortam oluştur ve etkinleştir (önerilir):

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Gerekli paketleri yükle:

   ```bash
   pip install -r requirements.txt
   ```

4. Uygulamayı başlat:

   ```bash
   flask run
   ```

   Uygulama `http://127.0.0.1:5000` adresinde açılır. Paneli görüntülemek için bu adresi tarayıcına gir.

CoinGecko’nun herkese açık API’si kullanıldığı için `.env` dosyası veya API anahtarı yapılandırması gerekmez.

---

## Crypto Tracker Platform

A dynamic cryptocurrency tracking dashboard built with Python (Flask) and JavaScript (Chart.js). It fetches market data from the free CoinGecko API and presents it in a responsive, dark-themed interface built with Bootstrap 5.

### Features

- **Live market data:** View the top 50 cryptocurrencies ranked by market capitalization.
- **Dynamic styling:** Display 24-hour price changes in green for gains and red for losses.
- **Search:** Instantly filter coins by name or symbol (e.g., BTC, Ethereum).
- **Coin details:** View statistics such as market capitalization, 24-hour trading volume, circulating supply, all-time high, and all-time low.
- **Interactive price charts:** Visualize the past 7 days of price data in an interactive Chart.js line chart.
- **API caching:** An in-memory cache helps reduce API requests during frequent page reloads.

### Tech Stack

- **Backend:** Python 3, Flask, `requests`
- **Frontend:** HTML5, CSS3, Jinja2, Bootstrap 5, Chart.js
- **External API:** [CoinGecko API v3](https://www.coingecko.com/en/api) (no API key required)

### Setup and Installation

Follow these steps to run the project locally.

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/crypto-tracker.git
   cd crypto-tracker
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   flask run
   ```

The application will be available at `http://127.0.0.1:5000`. Open this address in your browser to view the dashboard.

Since the project uses CoinGecko’s public API, no `.env` file or API key configuration is required.
