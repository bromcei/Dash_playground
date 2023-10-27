from dash import dcc, html
from Services.stats_processor import StatsCalc
from Pages.Filters.topline_filters import top_line_filter_q


def HypothesisPage(data_obj):
    stats_calc = StatsCalc()
    categorical_test = data_obj.get_columns(exlude=["year", "price",])
    return html.Div(
        [
            top_line_filter_q(data_obj),
            html.H1('Two Subsamples Hypothesis Testing'),
            html.Div([
                html.Div([
                    html.H2("Hypothesis Subset"),
                    dcc.Dropdown(
                        categorical_test,
                        categorical_test[0],
                        multi=False,
                        id='categorical-test-dropdown'),
                    html.Div([
                        html.P("Please Select Two Comparable Sets"),
                        html.Div([
                            dcc.Dropdown(
                                multi=False,
                                id='first-subset-dropdown')
                        ], style={"width": "50%"}),
                        html.Div([
                            dcc.Dropdown(
                                multi=False,
                                id='second-subset-dropdown')
                        ], style={"width": "50%"})

                    ],  style={"display":"flex"}),
                    html.P("Test Names:"),
                    dcc.RadioItems(
                        id='avalaible-tests',
                        options=stats_calc.get_two_ind_tests(),
                        value=stats_calc.get_two_ind_tests()[0],
                        inline=True
                    ),
                    html.H2("Checking if two selected subsets are Normally Distrubuted(D’Agostino and Pearson’s test)"),
                    html.P(id="norm-dist-hypothesis-1"),
                    html.P(id="norm-dist-hypothesis-2"),
                    html.H2("Testing hypothesis:"),
                    html.Li([], id="hypothesis-text", style={'list-style-type': 'none'}),
                    html.H2("Results:"),
                    html.P(id="hypothesis-result")
                ], style={"width": "50%"}),
                html.Div([
                    html.H2("Subsets Histogram"),
                    html.P("Histogram n bins slicer"),
                    dcc.Slider(5, 100, 5, id="hist-bins-slider", value=20, marks=None,
                               tooltip={"placement": "bottom", "always_visible": True}),
                    dcc.Graph(id="histogram-graph")
                ], style={"width": "50%"})
            ], style={"display": "flex"})
        ], style={'width': "100%"})
