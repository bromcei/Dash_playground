from dash import dcc, html
from Services.data_src import DataProcessor

year_range = DataProcessor().get_year_range()


def top_line_filter():
    return html.Div([
        html.Div([
            html.P("Year"),
            dcc.RangeSlider(
                min=year_range[0],
                max=year_range[1],
                step=1,
                value=year_range,
                marks={i: str(i) for i in range(year_range[0], year_range[1], 2)},
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

        ], style={"width": "100%", "display": "flex"})
    ])

