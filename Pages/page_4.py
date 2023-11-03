from dash import dcc, html
from Pages.Filters.topline_filters import top_line_filter_q

def DataCorrelation(data_obj):
    return  html.Div(
        [
            top_line_filter_q(data_obj),
            html.Div([
                html.Div([
                    html.H1('Categorical Data Correlation'),
                    html.P(
                        "Calculate the correlation/strength-of-association of features in data-set with both categorical and continuous features"),
                    dcc.Loading(
                        id='loading-3',
                        type='circle',
                        children=[
                            dcc.Graph(id='cramer-corr-matrix')
                        ])
                ], style={"width": "50%"}),
                html.Div([
                    html.H1("Correlation by Selected Feature"),
                    dcc.RadioItems(
                        id='x-axis',
                        options=data_obj.get_columns(exlude=["price", "year"]),
                        value=data_obj.get_columns(exlude=["price", "year"])[2],
                        inline=True
                    ),
                    dcc.Loading(
                        id='loading-3',
                        type='circle',
                        children=[
                            dcc.Graph(id='feature-corr-matrix')
                        ])

                ], style={"width": "50%"})
            ], style={"display": "flex"})
        ], style={'width': "100%"})