import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Access the API key
CMC_API_KEY = os.getenv("CMC_API_KEY")

BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

HEADERS = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": CMC_API_KEY
}
