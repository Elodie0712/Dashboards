import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# Import layouts and callbacks from tab1a, tab2a, and tab3a
from tab1a2 import layout as tab1_layout, register_callbacks as tab1_callbacks
from tab2ab import layout2 as tab2_layout, register_callbacks2 as tab2_callbacks
from tab3ab import layout3 as tab3_layout, register_callbacks3 as tab3_callbacks

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Define the main layout with tabs
app.layout = dbc.Container([
    dcc.Tabs([
        dcc.Tab(label='Tab 1: Overview', children=[tab1_layout()]),
        dcc.Tab(label='Tab 2: Student Performance', children=[tab2_layout()]),
        dcc.Tab(label='Tab 3: Sped and EB', children=[tab3_layout()])
    ])
], fluid=True)

# Register callbacks for all tabs
tab1_callbacks(app)
tab2_callbacks(app)
tab3_callbacks(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8059)
