from dash import dcc, html
from Pages.Filters.topline_filters import top_line_filter
def ML_layout(data_obj):
    return html.Div([
        html.H1('ML Training '),
        html.P("Data is preparing")

    ], style={'overflowX': 'scroll', 'width': "100%"})