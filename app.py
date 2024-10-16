import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from production_data import get_station_data

# Initialize the Dash app
app = dash.Dash("Manufacturing Workflow Dashboard")

# Get the data from production_data.py
stations, units = get_station_data()  # Simulated data
df = pd.DataFrame({'Station': stations, 'Units': units})

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Manufacturing Workflow Dashboard'),

    dcc.Graph(
        id='units-graph',
        figure=px.bar(df, x='Station', y='Units', title='Units at Each Production Station')
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
