from dash import dcc, html, dash_table
from Pages.Filters.topline_filters import top_line_filter

def Overview_layout(data_obj):
    return html.Div([
        top_line_filter(data_obj),
        html.H2('Average Vehicle Price and Vehicle Count over the Years '),
            html.Div([
                dcc.Loading(
                    id='loading-3',
                    type='circle',
                    children=[dash_table.DataTable(id="basic-info-table")])
            ]),
            html.Div([
                dcc.Loading(
                    id='loading-3',
                    type='circle',
                    children=[
                        dcc.Graph(id="bar-line-graph")
                        ])
            ]),
        html.H2("Vehicle Market Analysis by Selected Feature"),
        html.Div([
            html.Div([
                html.P("Select Feature"),
                dcc.RadioItems(
                    id='x-axis',
                    options=data_obj.get_columns(exlude=["price", "year"]),
                    value=data_obj.get_columns(exlude=["price", "year"])[0],
                    inline=True
                )
            ], style={"width": "25%"}),
            html.Div([
                html.P("N Comparission Year"),
                dcc.Slider(1, 30, 1, id="year-comp-slider", value=1, marks=None,
                           tooltip={"placement": "bottom", "always_visible": True})
            ], style={"width": "25%"}),

        ], style={"display":"flex"}),

        html.Div([
            html.Div([
                dcc.Loading(
                    id='loading-3',
                    type='circle',
                    children=[
                        dash_table.DataTable(
                            id='make-table',
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            page_current=0,
                            page_size=10
                        )
                        ])
            ], style={"width": "100%", 'overflowX': 'scroll'}),
        ], style={"display": "flex"})
        # html.H2('Box Plots by Selected Category'),
        # dcc.Graph(id="box-graph", style={"width": "100%", 'overflowX': 'scroll'}),

    ], style={'width': "100%"})
