# bokeh_stock_prices/overlay_multiple_stocks.py
# Illustrates overlaying multiple stock prices on a single chart for easy comparison

from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh_stock_prices.fetch_stock_data import fetch_stock_data
from bokeh_stock_prices.config import ALPHA_VANTAGE_API_KEY

# Function to run the overlay multiple stocks example
def run_overlay_multiple_stocks_example():
    symbols = ["AAPL", "GOOGL", "MSFT"]
    colors = ["blue", "green", "red"]

    # Create a Bokeh figure
    p = figure(title="Overlay Multiple Stocks", x_axis_label="Date", y_axis_label="Closing Price",
               x_axis_type="datetime", sizing_mode="stretch_width", toolbar_location="above")

    for symbol, color in zip(symbols, colors):
        stock_data = fetch_stock_data(symbol, interval="1d", output_size="compact")
        if stock_data is not None:
            # Plot the closing price as a line for each stock
            p.line(stock_data.index, stock_data["4. close"], line_width=2, legend_label=symbol,
                   color=color, line_dash="solid")

    # Add HoverTool for displaying additional information on hover
    hover = HoverTool()
    hover.tooltips = [("Date", "@x{%F}"), ("Closing Price", "@y{0.00}")]
    hover.formatters = {"@x": "datetime"}
    p.add_tools(hover)

    # Customize chart appearance
    p.title.text_font_size = "16pt"
    p.legend.label_text_font_size = "12pt"
    p.xaxis.axis_label_text_font_size = "12pt"
    p.yaxis.axis_label_text_font_size = "12pt"



    # Show the plot
    show(p)

# Example Usage:
# run_overlay_multiple_stocks_example()
