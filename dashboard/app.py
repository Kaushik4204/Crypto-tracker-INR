import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Ensure Python can find the src package
parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent not in sys.path:
    sys.path.insert(0, parent)

from src.fetch_data import fetch_crypto_data

# Page setup
st.set_page_config(layout="wide")
st.title("📊 Real-Time Crypto Dashboard (INR)")

# Fetch crypto data
data = fetch_crypto_data(50)

# Convert to DataFrame
df = pd.DataFrame([{
    "Name": c["name"],
    "Symbol": c["symbol"],
    "Price (INR)": round(c["quote"]["INR"]["price"], 2),
    "24h % Change": round(c["quote"]["INR"]["percent_change_24h"], 2),
    "Market Cap (₹ B)": round(c["quote"]["INR"]["market_cap"] / 1e9, 2),
    "Volume (24h, ₹ B)": round(c["quote"]["INR"]["volume_24h"] / 1e9, 2)
} for c in data])

# Full table
st.dataframe(df.sort_values("Market Cap (₹ B)", ascending=False), use_container_width=True)

st.divider()

# 📊 Top 10 Price Comparison
st.subheader("📊 Price Comparison of Top 10 Cryptos")
fig = px.bar(
    df.sort_values("Market Cap (₹ B)", ascending=False).head(10),
    x="Symbol", y="Price (INR)", color="Symbol", text="Price (INR)",
    title="Top 10 Cryptos by Price"
)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# 📈 24h % Change Line Chart
st.subheader("📈 24h % Change (Top 10)")
fig2 = px.line(
    df.sort_values("Market Cap (₹ B)", ascending=False).head(10),
    x="Symbol", y="24h % Change", markers=True,
    title="24h Price Change Trend"
)
st.plotly_chart(fig2, use_container_width=True)

st.divider()

# 🚀 Top Gainers
st.subheader("🚀 Top Gainers (24h)")
st.dataframe(df.sort_values("24h % Change", ascending=False).head(5), use_container_width=True)

# 📉 Top Losers
st.subheader("📉 Top Losers (24h)")
st.dataframe(df.sort_values("24h % Change").head(5), use_container_width=True)
