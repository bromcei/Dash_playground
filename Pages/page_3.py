from dash import dcc, html, dash_table


# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import pandas as pd
# from datetime import date, datetime, timedelta


def page_3_layout():
    return html.Div([
            html.H1("db-edata Server Validations"),
            html.P(f"Missing ICD codes in [Heap].[foxus].[eRx] table: {', '.join(erx_missing_icds)}"),
            html.P(f"Missing hcp_ids in eRxs tale: {missing_hcps.shape[0]}"),
            html.P(f"Unknown PackageID's(not in SSA_TSA) in eRx's table: {missing_package_id}"),
            html.P("Last eRx date:"),
            html.P(id='rxs-last-date-month'),
            html.P("Last visit date:"),
            html.P(id='visit-last-date-month'),
            html.P("Rxs Count by date"),
            html.Div([
                dcc.Graph(
                    id='rxs-data-month'
                ),
                dcc.Interval(
                    id='interval-rxs-data',
                    interval=3600 * 1000,  # miliseconds
                    n_intervals=0
                )
            ],
                style={
                    # 'width': 1000,
                    # 'display:': 'inline',
                    'overflowY': 'scroll'}
            ),
            html.Div([
                dcc.Graph(
                    id='visit-data-month'
                ),
                dcc.Interval(
                    id='interval-rxs-data',
                    interval=3600 * 1000,  # miliseconds
                    n_intervals=0
                )
            ],
                style={
                    # 'width': 1000,
                    # 'display:': 'inline',
                    'overflowY': 'scroll'}
            ),
            html.Div([
                dash_table.DataTable(missing_hcps.to_dict('records'),
                                     [{"name": i, "id": i} for i in missing_hcps.columns],
                                     style_cell_conditional=[
                                         {'if': {'column_id': 'hcp_id'},
                                          'width': '100px'},
                                         {'if': {'column_id': 'healthcare_provider_id'},
                                          'width': '100px'},
                                         {'if': {'column_id': 'health_care_provider_name'},
                                          'width': '250px'}
                                     ]
                                     )
            ],
                style={
                    'width': 1000,
                    'overflowY': 'scroll'}
            )
        ])