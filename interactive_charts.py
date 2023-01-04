# bokeh_stock_prices/interactive_charts.py
# Demonstrates creating interactive line charts using Bokeh with zooming and panning capabilities



# Function to run the interactive charts example
def run_interactive_charts_example():
    stock_symbol = "AAPL"
    stock_data = fetch_stock_data(stock_symbol, interval="1d", output_size="compact")

    if stock_data is not None:
        # Create a Bokeh figure
        p = figure(title=f"{stock_symbol} Stock Price", x_axis_label="Date", y_axis_label="Closing Price",
                   x_axis_type="datetime", sizing_mode="stretch_width", toolbar_location="above")

        # Plot the closing price as a line
        p.line(stock_data.index, stock_data["4. close"], line_width=2, legend_label="Closing Price", color="blue")

        # Add HoverTool for displaying additional information on hover

# Example Usage:
# run_interactive_charts_example()
