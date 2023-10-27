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
        html.H2("Vehicle Brands and Models Market Analysis"),
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
            ], style={"width": "60%"}),
            html.Div([
                dash_table.DataTable(
                    id='model-table',
                    filter_action="native",
                    sort_action="native",
                    sort_mode='multi',
                    page_current=0,
                    page_size=10
                )
            ], style={"width": "40%", "padding-lef": "20px"}),

        ], style={"display": "flex"}),
        html.H2('Box Plots by Selected Category'),
        dcc.RadioItems(
            id='x-axis',
            options=data_obj.get_columns(exlude=["price", "year"]),
            value=data_obj.get_columns(exlude=["price", "year"])[-2],
            inline=True
        ),
        dcc.Graph(id="box-graph"),

    ], style={'overflowX': 'scroll', 'width': "100%"})
