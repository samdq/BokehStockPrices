# bokeh_stock_prices/customize_chart_appearance.py
# Showcases customizing chart appearance using color palettes and annotations

from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, Band, Label
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh_stock_prices.fetch_stock_data import fetch_stock_data
from bokeh_stock_prices.config import ALPHA_VANTAGE_API_KEY

# Function to run the customize chart appearance example
def run_customize_chart_appearance_example():
    stock_symbol = "AAPL"
    stock_data = fetch_stock_data(stock_symbol, interval="1d", output_size="compact")

    if stock_data is not None:
        # Create a Bokeh figure
        p = figure(title=f"{stock_symbol} Stock Price with Custom Appearance", x_axis_label="Date",
                   y_axis_label="Closing Price", x_axis_type="datetime", sizing_mode="stretch_width",
                   toolbar_location="above")

        # Plot the closing price as a line
        p.line(stock_data.index, stock_data["4. close"], line_width=2, legend_label="Closing Price", color="blue")

        # Add HoverTool for displaying additional information on hover
        hover = HoverTool()
        hover.tooltips = [("Date", "@x{%F}"), ("Closing Price", "@y{0.00}")]
        hover.formatters = {"@x": "datetime"}
        p.add_tools(hover)



        # Add a shaded region for a specific time period (e.g., market downturn)
        downturn_start_date = pd.to_datetime("2022-01-01")
        downturn_end_date = pd.to_datetime("2022-04-01")
        downturn_band = Band(base="x", lower=downturn_start_date, upper=downturn_end_date,
                             level="underlay", fill_alpha=0.1, fill_color="red", line_color=None)
        p.add_layout(downturn_band)

        # Add a label annotation
        label = Label(x=pd.to_datetime("2022-03-01"), y=stock_data["4. close"].max(), text="Market Downturn",
                      render_mode="css", text_font_size="12pt", text_color="red")
        p.add_layout(label)

        # Embed the Bokeh plot in an HTML file
        output_file("customize_chart_appearance_chart.html")

        # Show the plot
        show(p)

# Example Usage:
# run_customize_chart_appearance_example()