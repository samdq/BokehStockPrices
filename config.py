
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

# Example Usage:
# api_key = Config.ALPHA_VANTAGE_API_KEY
# data_directory = Config.get_data_dir()
# templates_directory = Config.get_templates_dir()
# static_directory = Config.get_static_dir()
