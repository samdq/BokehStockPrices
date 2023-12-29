# bokeh_stock_prices/overlay_multiple_stocks.py
# Illustrates overlaying multiple stock prices on a single chart for easy comparison



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

    # Show the legend
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"

    # Embed the Bokeh plot in an HTML file
    output_file("overlay_multiple_stocks_chart.html")

    # Show the plot
    show(p)

# Example Usage:
# run_overlay_multiple_stocks_example()
