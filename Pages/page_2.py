from dash import dcc, html, dash_table
from Pages.Filters.topline_filters import top_line_filter

def Overview_layout(data_obj):
    return html.Div([
        top_line_filter(data_obj),
        html.H2('Average Vehicle Price and Vehicle Count over the Years '),
            html.Div([
                dash_table.DataTable(
                    id="basic-info-table")
            ]),
            html.Div([
                dcc.Graph(id="bar-line-graph")
            ]),
        html.H2("Vehicle Market Analysis by Selected Feature"),
        dcc.RadioItems(
            id='x-axis',
            options=data_obj.get_columns(exlude=["price"]),
            value=data_obj.get_columns(exlude=["price"])[1],
            inline=True
        ),
        html.Div([
            html.Div([
                dash_table.DataTable(
                    id='make-table',
                    filter_action="native",
                    sort_action="native",
                    sort_mode='multi',
                    page_current=0,
                    page_size=10
                )
            ], style={"width": "100%", 'overflowX': 'scroll'}),
        ], style={"display": "flex"})
        # html.H2('Box Plots by Selected Category'),
        # dcc.Graph(id="box-graph", style={"width": "100%", 'overflowX': 'scroll'}),

    ], style={'width': "100%"})
