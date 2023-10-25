from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from Pages.Nav.top_nav import top_nav
from Services.data_src import DataProcessor
from Pages.page_1 import DataQualityLayout
from Pages.page_2 import Overview_layout
from Pages.page_3 import HypothesisPage
from Pages.page_4 import ML_layout
from scipy.stats import normaltest


app = Dash(__name__, suppress_callback_exceptions=True)
app.title = 'CarVertical Homework'

#Data
data_obj = DataProcessor()


app.layout = top_nav

@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return DataQualityLayout(data_obj)

    if tab == 'tab-2':
        return Overview_layout(data_obj)

    elif tab == 'tab-3':
        return HypothesisPage(data_obj)

    elif tab == 'tab-4':
        return ML_layout(data_obj)


# Page 2 ---------------------------------------------------------------------------------------------------------------
@app.callback(Output('bar-line-graph', 'figure'),
            [
                Input("year-range", "value"),
                Input("make-dropdown", "value"),
                Input("model-dropdown", "value"),
                Input("transmission-dropdown", "value"),
                Input("fuel-dropdown", "value"),
                Input("color-dropdown", "value")
             ])
def line_bar_chart(year, make, model, transmission, fuel, color):
    return data_obj.bar_line_chart_ov(year, make, model, transmission, fuel, color)
@app.callback(Output('box-graph', 'figure'),
            [
                Input("x-axis", "value"),
                Input("year-range", "value"),
                Input("make-dropdown", "value"),
                Input("model-dropdown", "value"),
                Input("transmission-dropdown", "value"),
                Input("fuel-dropdown", "value"),
                Input("color-dropdown", "value")
             ])
def box_plot_by_cat(x, year, make, model, transmission, fuel, color):
    return data_obj.box_plot_ov(x, year, make, model, transmission, fuel, color)

# Page 3 ---------------------------------------------------------------------------------------------
@app.callback(
    Output('first-subset-dropdown', 'options'),
            [
                Input("categorical-test-dropdown", "value"),
            ])
def first_subset_values(value):
    return data_obj.get_col_unique_values(value)

@app.callback(Output('second-subset-dropdown', 'options'),
            [
                Input("categorical-test-dropdown", "value"),
             ])
def second_subset_values(value):
    return data_obj.get_col_unique_values(value)

@app.callback(
    [
        Output('histogram-graph', 'figure'),
        Output('norm-dist-hypothesis-1', 'children'),
        Output('norm-dist-hypothesis-2', 'children'),
        Output('hypothesis-text', 'children'),
        Output('hypothesis-result', 'children'),
    ],
    [
        Input("year-range", "value"),
        Input("make-dropdown", "value"),
        Input("model-dropdown", "value"),
        Input("transmission-dropdown", "value"),
        Input("fuel-dropdown", "value"),
        Input("color-dropdown", "value"),
        Input("quantile-range", "value"),
        Input("categorical-test-dropdown", "value"),
        Input("first-subset-dropdown", "value"),
        Input("second-subset-dropdown", "value"),
        Input("avalaible-tests", "value")
     ])
def hist_chart(year, make, model, transmission, fuel, color, quantile_range, category_name, category_value_1, category_value_2, test_name):
    return data_obj.hist_plot(year, make, model, transmission, fuel, color, quantile_range, category_name, category_value_1, category_value_2, test_name)



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
