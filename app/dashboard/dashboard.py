from dash import Dash, html, dcc
from .callbacks import get_callbacks
import os
def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets=[
            '/static/css/bootstrap.min.css',
            '/static/css/styles.css',
        ]
    )

    with open('/Users/hy/Library/Mobile Documents/com~apple~CloudDocs/workspace/dash-flask-test/app/templates/dashboard.html', 'r') as f:
        html_string = f.read()

    dash_app.index_string = html_string
    dash_app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),
    ])

    get_callbacks(dash_app)

    return dash_app