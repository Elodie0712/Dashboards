import dash
import dash_bootstrap_components as dbc
from tab1a import layout as tab1_layout, register_callbacks as tab1_callbacks

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Set the layout
app.layout = tab1_layout()

# Register callbacks
tab1_callbacks(app)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8059)
