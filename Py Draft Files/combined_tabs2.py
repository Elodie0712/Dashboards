# main_app.py

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# Import layouts and callbacks from tab1a and tab2a
from tab1a2 import layout as tab1_layout, register_callbacks as tab1_callbacks
from tab2a import layout2 as tab2_layout, register_callbacks2 as tab2_callbacks

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Define the main layout with two tabs
app.layout = dbc.Container([
    dcc.Tabs([
        dcc.Tab(label='Tab 1: Overview', children=tab1_layout()),
        dcc.Tab(label='Tab 2: Student Performance', children=tab2_layout())
    ])
], fluid=True)

# Register callbacks for both tabs
tab1_callbacks(app)
tab2_callbacks(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8059)
