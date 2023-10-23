from dash import dcc, html, dash_table


# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import pandas as pd
# from datetime import date, datetime, timedelta


def page_2_layout():
    return html.Div([
            # Set the new white-text image
            html.H1('Telemetry Production Server'),
            html.Div(
                className='sidenav',
                children=[
                    html.Div(
                        className='dropdown',
                        children=[
                            html.P("Patient Group"),
                            dcc.Dropdown(
                                ['NYC', 'MTL', 'SF'],
                                'NYC',
                                id='demo-dropdown',
                                multi=True,
                                clearable=False
                            )
                        ]
                    ),
                    html.Div(
                        className='dropdown',
                        children=[
                            html.P("Metric Name"),
                            dcc.Dropdown(
                                ['NYC', 'MTL', 'SF'],
                                'NYC',
                                id='demo-dropdown',
                                multi=True,
                                clearable=False
                            )
                        ]
                    ),
                    html.Div(
                        className='dropdown',
                        children=[
                            html.P("Patients"),
                            dcc.Dropdown(
                                ['NYC', 'MTL', 'SF'],
                                'NYC',
                                id='demo-dropdown',
                                multi=True,
                                clearable=False
                            )
                        ]
                    )
            ]),
            html.Div(
                className='main',
                children = [
                html.P('Mainas')
            ]
            ),

    ])
            # html.Div([
            #     "Select patient_id:",
            #     dcc.Dropdown(
            #         id='patient-id-opt-dropdown',
            #         searchable=True
            #     ),
            # ], style={'width': '20%', 'display': 'inline-block'}
            # ),
            # html.Div([
            #     "Select user_id:",
            #     dcc.Dropdown(
            #         id='user-id-opt-dropdown',
            #         searchable=True
            #     ),
            # ], style={'width': '20%', 'display': 'inline-block'}
            # ),
