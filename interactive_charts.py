# bokeh_stock_prices/interactive_charts.py
# Demonstrates creating interactive line charts using Bokeh with zooming and panning capabilities



# Function to run the interactive charts example
def run_interactive_charts_example():
    stock_symbol = "AAPL"
    stock_data = fetch_stock_data(stock_symbol, interval="1d", output_size="compact")



        # Plot the closing price as a line
        p.line(stock_data.index, stock_data["4. close"], line_width=2, legend_label="Closing Price", color="blue")

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

        # Embed the Bokeh plot in an HTML file
        output_file("interactive_chart.html")

        # Show the plot
        show(p)

# Example Usage:
# run_interactive_charts_example()
