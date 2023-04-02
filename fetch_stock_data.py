# bokeh_stock_prices/fetch_stock_data.py
# Logic to fetch historical stock data from the Alpha Vantage API

import os
import requests
import pandas as pd
from bokeh_stock_prices.config import ALPHA_VANTAGE_API_KEY

# Function to fetch historical stock data from Alpha Vantage API
def fetch_stock_data(symbol, interval="1d", output_size="compact"):
    try:
        # API endpoint and parameters
        api_url = "https://www.alphavantage.co/query"
        function = "TIME_SERIES_INTRADAY" if interval == "1d" else "TIME_SERIES_DAILY"
        params = {
            "function": function,
            "symbol": symbol,
            "interval": interval,
            "apikey": ALPHA_VANTAGE_API_KEY,
            "outputsize": output_size,
        }
        # Make API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        # Parse response JSON into DataFrame

        else:
            print(f"Error: {data['Note']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None

# Example Usage:
# stock_symbol = "AAPL"
# stock_data = fetch_stock_data(stock_symbol, interval="1d", output_size="compact")
# print(stock_data.head())