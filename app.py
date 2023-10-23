from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import graphs
from Services.data_src import DataProcessor
from Pages.page_1 import page_1_layout
from Pages.page_2 import page_2_layout

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = 'CarVertical Homework'

#Data
data_obj = DataProcessor()

# Tables and Graphs Parameters
PAGE_SIZE = 10
n_days = 90

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'color': 'black',
    'backgroundColor': '#EEEEEE',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#106669',
    'color': 'white',
    'padding': '6px'
}

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Data Quality and Data Visualization', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Hypothesis Testing', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='ML ', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 4', value='tab-4', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])


@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return page_1_layout()

    if tab == 'tab-2':
        return page_2_layout()


    elif tab == 'tab-3':
        return 0

    elif tab == 'tab-4':
        return 0


# Page 1 ---------------------------------------------------------------------------------------------------------------
@app.callback(Output('box-graph', 'figure'),
            [Input("x-axis", "value")])
def box_plot_by_cat(x):
    return data_obj.box_plot(x)

# @app.callback(Output('parsed-data', 'figure'),
#               Input('interval-parsed-data', 'n_intervals'))
# def update_parsed_data(n):
#     return graphs.telemetryWika_live_stream()
#
#
#
#
# @app.callback([
#     Output('rxs-data', 'figure'),
#     Output('rxs-last-date', 'children')],
#     [Input('interval-rxs-data', 'n_intervals')])
# def update_rxs_data(n):
#     fig, last_recipe_date = graphs.erx_fig(n_months=home_n_months)
#     return fig, last_recipe_date
#
#
# @app.callback([
#     Output('rxs-data-month', 'figure'),
#     Output('rxs-last-date-month', 'children')],
#     [Input('interval-rxs-data', 'n_intervals')])
# def update_rxs_data_month(n):
#     fig, last_recipe_date = graphs.erx_fig(n_months=home_n_months)
#     return fig, last_recipe_date
#
#
# @app.callback([
#     Output('visit-data', 'figure'),
#     Output('visit-last-date', 'children')],
#     [Input('interval-rxs-data', 'n_intervals')])
# def update_visit_data(n):
#     fig, last_visit_date = graphs.visits_fig(n_months=home_n_months)
#     return fig, last_visit_date
#
# @app.callback(
#     Output('missing-specialities-eRx', 'children'),
#     [Input('interval-rxs-data', 'n_intervals')])
# def update_visit_data(n):
#     return graphs.missing_spec()
#
# @app.callback(
#     Output('missing-hcps-eRx', 'children'),
#     [Input('interval-rxs-data', 'n_intervals')])
# def update_visit_data(n):
#     return graphs.missing_hcps()
#
# @app.callback(
#     Output('missing-specs-line', 'figure'),
#     [Input('interval-rxs-data', 'n_intervals')])
# def update_rxs_data(n):
#     fig = graphs.missing_spec_line_plot()
#     return fig
#
# @app.callback(
#     Output('missing-hcps-line', 'figure'),
#     [Input('interval-rxs-data', 'n_intervals')])
# def update_rxs_data(n):
#     fig = graphs.missing_hcp_line_plot()
#     return fig
# ----------------------------------------------------------------------------------------------------------------------


# 2 Page ---------------------------------------------------------------------------------------------------------------





if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
