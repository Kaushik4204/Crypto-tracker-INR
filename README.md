# 📊 Crypto Tracker INR 🇮🇳

A professional real-time dashboard to monitor the **top 50 cryptocurrencies** using the [CoinMarketCap API](https://coinmarketcap.com/api/) — with INR conversion, interactive charts, and auto-save functionality.

---

## 🚀 Features

- ✅ Real-time top 50 cryptocurrency data (price, volume, market cap)
- 📈 Interactive charts: bar chart + 24h change line chart
- 💾 Auto-save daily data to CSV via scheduler
- 🇮🇳 INR currency support
- ☁️ Ready for deployment on **Streamlit Cloud**
- 📁 Clean modular codebase: `src/`, `dashboard/`, `scheduler/`

---

🖼️ Dashboard Preview
<img width="1365" height="574" alt="image" src="https://github.com/user-attachments/assets/b52b0a11-0ae5-478c-b2b1-e5d455a8264c" />
<img width="1360" height="513" alt="image" src="https://github.com/user-attachments/assets/df2335d2-e79a-4311-9173-3a39e5e2ec8d" />
<img width="1365" height="536" alt="image" src="https://github.com/user-attachments/assets/19249be9-7103-407f-8e87-a90938bae446" />
<img width="1361" height="620" alt="image" src="https://github.com/user-attachments/assets/26037acb-5d70-4ebb-8912-005fa55016a8" />

#  Project Structure

crypto-tracker/
├── dashboard/

│ └── app.py # Streamlit app entry

│

├── data/

│ └── crypto_prices.csv # Saved daily snapshots

│

├── scheduler/

│ └── daily_scraper.py # Scheduled fetch & save

│

├── src/

│ ├── fetch_data.py

│ ├── save_data.py

│ ├── config.py

│ └── init.py

│

├── .streamlit/

│ └── secrets.toml # For Streamlit Cloud API key

│

├── .env # Local API key (ignored in git)

├── .gitignore

├── requirements.txt

└── README.md

---

Setup Instructions

1. Clone the repo

 ```bash
git clone https://github.com/Kaushik4204/Crypto-tracker-INR.git
cd Crypto-tracker-INR
  ```

2. Create a virtual environment (optional but recommended)

 ```bash
python -m venv venv
venv\Scripts\activate  # On Windows
 ```

4. Install dependencies

 ```bash
pip install -r requirements.txt
 ```

5. Add your API key
Create a .env file in the root directory:
CMC_API_KEY=your_coinmarketcap_api_key

---

💻 Run Locally:
streamlit run dashboard/app.py

Daily Data Capture
To save crypto prices daily at 8:00 AM (can be modified):
python scheduler/daily_scraper.py

---

📌 Notes
The .env file is excluded via .gitignore to keep your API key safe.
All interactive charts are created using Plotly.
The project supports INR (₹) conversion directly via the API.

---

Contact:
Built by Kaushik Puli
Email: 2021.kaushik.puli@ves.ac.in


