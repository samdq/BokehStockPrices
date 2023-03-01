# bokeh_stock_prices/__init__.py
# Initialization file for the BokehStockPrices module

import os

# Ensure that the 'data' directory exists
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Ensure that the 'templates' directory exists
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# Ensure that the 'static' directory exists
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# Additional initialization code can be added here based on project requirements
# For example, setting up logging, initializing database connections, etc.
