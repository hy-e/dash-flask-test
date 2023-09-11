from dash import Dash, html, dcc
from dash_extensions import Mermaid


def build_details():
    details = []

    # title
    details += [html.H2("Details")]

    # flow chart
    details += [html.Div([
                    html.Div('PV', className='chart-done chart-col', id='pv-flow'),
                    html.Div(className='chart-line-h'),
                    html.Div('MV', className='chart-done chart-col', id='mv-flow'),
                    html.Div(className='chart-line-h'),
                    html.Div('양산MTO', className='chart-done chart-col', id='mto-flow'),
                    html.Div(className='chart-line-h'),
                    html.Div('PRA', className='chart-pill chart-col', id='pra-flow'),
                    html.Div(className='chart-line-h'),
                    html.Div('양산이관', className='chart-pill chart-col', id='sra-flow')]
                ,className='chart-row')]

    # summary table

    



    return details