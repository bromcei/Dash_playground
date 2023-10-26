from dash import dcc, html
from Pages.Filters.topline_filters import top_line_filter
def DataQualityLayout(data_obj):
    return html.Div([
        html.H1('Data Quality Overview '),
        html.P("Data is preparing"),
        html.Iframe(src=r'assets/page1.html', style={"frameBorder": "0", "height": "100%", "width": "100%"},)
    ], style={"border": "none", 'width': "100%", "height": "100vh"})