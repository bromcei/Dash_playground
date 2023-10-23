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
                id='year-range')
        ], style={"width": "100%"}),
        html.Div([
            html.Div([
                html.P("Make"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("make"),
                    None,
                    multi=True,
                    id='make-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Model"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("model"),
                    None,
                    multi=True,
                    id='model-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Transmission"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("transmission"),
                    None,
                    multi=True,
                    id='transmission-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Fuel"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("fuel"),
                    None,
                    multi=True,
                    id='fuel-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Color"),
                dcc.Dropdown(
                    DataProcessor().get_col_unique_values("color"),
                    None,
                    multi=True,
                    id='color-dropdown')
            ], style={"width": "20%"})

        ], style={"width": "100%", "display": "flex"}),

        html.H1('Box Plots by Selected Category'),
        dcc.RadioItems(
            id='x-axis',
            options=DataProcessor().get_columns(exlude=["price", "year", "make", "model"]),
            value=DataProcessor().get_columns(exlude=["price", "year", "make", "model"])[1],
            inline=True
        ),
        dcc.Graph(id="box-graph"),

    ], style={'overflowX': 'scroll', 'width': "100%"})
