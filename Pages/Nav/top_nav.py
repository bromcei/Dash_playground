from dash import dcc, html
import assets.tab_styles_config as tsc

top_nav = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Data Quality', value='tab-1', style=tsc.tab_style, selected_style=tsc.tab_selected_style),
        dcc.Tab(label='Data Overview', value='tab-2', style=tsc.tab_style, selected_style=tsc.tab_selected_style),
        dcc.Tab(label='Hypothesis Testing', value='tab-3', style=tsc.tab_style, selected_style=tsc.tab_selected_style),
        dcc.Tab(label='ML', value='tab-4', style=tsc.tab_style, selected_style=tsc.tab_selected_style),
    ], style=tsc.tabs_styles),
    html.Div(id='tabs-content-inline')
])