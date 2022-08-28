# bokeh_stock_prices/config.py
# Configuration settings, including the Alpha Vantage API key
# Remember to keep this file private

import os

class Config:
    ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"

    @staticmethod
    def get_data_dir():
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(data_dir, exist_ok=True)
        return data_dir

    @staticmethod
    def get_templates_dir():
        templates_dir = os.path.join(os.path.dirname(__file__), "templates")
        os.makedirs(templates_dir, exist_ok=True)
        return templates_dir

    @staticmethod
    def get_static_dir():
        static_dir = os.path.join(os.path.dirname(__file__), "static")
        os.makedirs(static_dir, exist_ok=True)
        return static_dir


