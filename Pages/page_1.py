from dash import dcc, html
from Services.data_src import DataProcessor


def page_1_layout():
    return html.Div([
        # Set the new white-text image
        html.Div([
            html.P("Year"),
            dcc.RangeSlider(
                min=1970,
                max=2023,
                step=1,
                value=[1970, 2023],
                marks={i: str(i) for i in range(1970, 2023, 2)},
                id='year-range')
        ], style={"width": "100%"}),
        html.Div([
            html.Div([
                html.P("Make"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("make"),
                    [],
                    multi=True,
                    id='make-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Model"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("model"),
                    [],
                    multi=True,
                    id='model-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Transmission"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("transmission"),
                    [],
                    multi=True,
                    id='transmission-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Fuel"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("fuel"),
                    [],
                    multi=True,
                    id='fuel-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Color"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("color"),
                    [],
                    multi=True,
                    id='color-dropdown')
            ], style={"width": "20%"})

        ], style={"width": "100%", "display": "flex"}),

        html.H1('Box Plots by Selected Category'),
        dcc.RadioItems(
            id='x-axis',
            options=DataProcessor().get_columns(exlude=["price", "year"]),
            value=DataProcessor().get_columns(exlude=["price", "year"])[1],
            inline=True
        ),
        dcc.Graph(id="box-graph"),

    ], style={'overflowX': 'scroll', 'width': "100%"})
