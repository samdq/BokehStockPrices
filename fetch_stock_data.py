# bokeh_stock_prices/fetch_stock_data.py
# Logic to fetch historical stock data from the Alpha Vantage API

import os
import requests
import pandas as pd
from bokeh_stock_prices.config import ALPHA_VANTAGE_API_KEY

# Function to fetch historical stock data from Alpha Vantage API


# Example Usage:
# stock_symbol = "AAPL"
# stock_data = fetch_stock_data(stock_symbol, interval="1d", output_size="compact")
# print(stock_data.head())