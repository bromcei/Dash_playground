from dash import dcc, html
from Services.data_src import DataProcessor
import numpy as np



def top_line_filter(data_obj):
    year_range = data_obj.get_year_range()
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
                    data_obj.get_col_unique_values("make"),
                    [],
                    multi=True,
                    id='make-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Model"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("model"),
                    [],
                    multi=True,
                    id='model-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Transmission"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("transmission"),
                    [],
                    multi=True,
                    id='transmission-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Fuel"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("fuel"),
                    [],
                    multi=True,
                    id='fuel-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Color"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("color"),
                    [],
                    multi=True,
                    id='color-dropdown')
            ], style={"width": "20%"})

        ], style={"width": "100%", "display": "flex"})
    ])

def top_line_filter_q(data_obj):
    year_range = data_obj.get_year_range()
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
                    data_obj.get_col_unique_values("make"),
                    [],
                    multi=True,
                    id='make-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Model"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("model"),
                    [],
                    multi=True,
                    id='model-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Transmission"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("transmission"),
                    [],
                    multi=True,
                    id='transmission-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Fuel"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("fuel"),
                    [],
                    multi=True,
                    id='fuel-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Color"),
                dcc.Dropdown(
                    data_obj.get_col_unique_values("color"),
                    [],
                    multi=True,
                    id='color-dropdown')
            ], style={"width": "20%"}),
            html.Div([
                html.P("Price Quantile Filter"),
                dcc.RangeSlider(
                    min=0,
                    max=1,
                    step=0.05,
                    value=[0.05, 0.95],
                    marks={i: f"{i:.2f}" for i in np.arange(0, 1, 0.1)},
                    id='quantile-range')
            ], style={"width": "20%"})

        ], style={"width": "100%", "display": "flex"})
    ])

