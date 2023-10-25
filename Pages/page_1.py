from dash import dcc, html
from Pages.Filters.topline_filters import top_line_filter
def DataQualityLayout(data_obj):
    return html.Div([
        html.H1('Data Quality Overview '),
        html.P("Data is preparing")

    ], style={'width': "100%"})