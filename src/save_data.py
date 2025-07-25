# src/save_data.py
import pandas as pd
from datetime import datetime

def save_to_csv(data, filename="data/crypto_prices.csv"):
    rows = []
    for coin in data:
        rows.append({
            "Timestamp": datetime.utcnow().isoformat(),
            "Name": coin["name"],
            "Symbol": coin["symbol"],
            "Price (USD)": coin["quote"]["USD"]["price"],
            "24h % Change": coin["quote"]["USD"]["percent_change_24h"],
            "Market Cap": coin["quote"]["USD"]["market_cap"],
            "Volume (24h)": coin["quote"]["USD"]["volume_24h"]
        })
    df = pd.DataFrame(rows)
    df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
