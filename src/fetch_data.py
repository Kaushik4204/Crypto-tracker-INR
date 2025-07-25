import requests
from src.config import BASE_URL, HEADERS

def fetch_crypto_data(limit=50):
    params = {"start": "1", "limit": str(limit), "convert": "INR"}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()["data"]
