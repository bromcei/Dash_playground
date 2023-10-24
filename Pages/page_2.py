from dash import dcc, html
from Services.data_src import DataProcessor
from Pages.Filters.topline_filters import top_line_filter

def Overview_layout(data_obj):
    return html.Div([
        top_line_filter(data_obj),
        html.H1('Average Vehicle Price and Vehicle Count over the Years '),
        dcc.Graph(id="bar-line-graph"),

        html.H1('Box Plots by Selected Category'),
        dcc.RadioItems(
            id='x-axis',
            options=data_obj.get_columns(exlude=["price", "year"]),
            value=data_obj.get_columns(exlude=["price", "year"])[1],
            inline=True
        ),
        dcc.Graph(id="box-graph"),

    ], style={'overflowX': 'scroll', 'width': "100%"})
