from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from .callbacks import get_callbacks
from .layout.details import build_details
import os
def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets=[
            '/static/css/bootstrap.min.css',
            '/static/css/styles.css',
            dbc.themes.BOOTSTRAP
        ]
    )

    with open('/Users/hy/Library/Mobile Documents/com~apple~CloudDocs/workspace/dash-flask-test/app/templates/dashboard.html', 'r') as f:
        html_string = f.read()

    dash_app.index_string = html_string
    dash_app.layout = html.Div(build_details())

    get_callbacks(dash_app)

    return dash_app