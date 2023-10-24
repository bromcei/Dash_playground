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
                    html.P("Hypothesis Subset"),
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
                    )
                ], style={"width": "50%"}),
                html.Div([
                    dcc.Graph(id="histogram-graph")
                ], style={"width": "50%"})
            ], style={"display": "flex"})
        ], style={'overflowX': 'scroll', 'width': "100%"})
