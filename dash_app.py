from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from Pages.Nav.top_nav import top_nav
from Services.data_src import DataProcessor
from Pages.page_1 import DataQualityLayout
from Pages.page_2 import Overview_layout
from Pages.page_3 import HypothesisPage
from Pages.page_4 import DataCorrelation
from plotly.validator_cache import ValidatorCache

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
        return DataCorrelation(data_obj)

    elif tab == 'tab-4':
        return HypothesisPage(data_obj)


# Page 2 ---------------------------------------------------------------------------------------------------------------
@app.callback([
            Output('bar-line-graph', 'figure'),
            # Output('box-graph', 'figure'),
            Output('make-table', 'data'),
            Output('make-table', 'columns'),
            Output('basic-info-table', 'data'),
            Output('basic-info-table', 'columns')
],
            [
                Input("year-range", "value"),
                Input("make-dropdown", "value"),
                Input("model-dropdown", "value"),
                Input("transmission-dropdown", "value"),
                Input("fuel-dropdown", "value"),
                Input("color-dropdown", "value"),
                Input("x-axis", "value"),
                Input("year-comp-slider", "value")

             ])
def line_bar_chart(year, make, model, transmission, fuel, color, x_boxaxis, n_year):
    return data_obj.bar_line_chart_ov(year, make, model, transmission, fuel, color, x_boxaxis, n_year)

# @app.callback(Output('box-graph', 'figure'),
#             [
#                 Input("x-axis", "value"),
#                 Input("year-range", "value"),
#                 Input("make-dropdown", "value"),
#                 Input("model-dropdown", "value"),
#                 Input("transmission-dropdown", "value"),
#                 Input("fuel-dropdown", "value"),
#                 Input("color-dropdown", "value")
#              ])
# def box_plot_by_cat(x, year, make, model, transmission, fuel, color):
#     return data_obj.box_plot_ov(x, year, make, model, transmission, fuel, color)

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
    Output('quantile-output', 'children'),
    Input('quantile-range', 'value')
)
def update_output(selected_range):
    return f'Selected Range: {selected_range[0]} - {selected_range[1]}'

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
        Input("avalaible-tests", "value"),
        Input("hist-bins-slider", "value"),
        Input("his-log-axis", "value")
     ])
def hist_chart(year, make, model, transmission, fuel, color, quantile_range, category_name, category_value_1, category_value_2, test_name, bin_size, hist_log_yaxis):
    return data_obj.hist_plot(year, make, model, transmission, fuel, color, quantile_range, category_name, category_value_1, category_value_2, test_name, bin_size, hist_log_yaxis)



@app.callback(
        [
            Output('cramer-corr-matrix', 'figure'),
            Output('feature-corr-matrix', 'figure')
         ],
    [
        Input("year-range", "value"),
        Input("make-dropdown", "value"),
        Input("model-dropdown", "value"),
        Input("transmission-dropdown", "value"),
        Input("fuel-dropdown", "value"),
        Input("color-dropdown", "value"),
        Input("quantile-range", "value"),
        Input("x-axis", "value")
     ])
def corr_plots(year, make, model, transmission, fuel, color, quantile_range, selected_feature):
    corr_matrix = data_obj.correlation_analysis(year, make, model, transmission, fuel, color, quantile_range, selected_feature)
    return corr_matrix


#
# if __name__ == '__main__':
#     app.run_server(host='0.0.0.0', port=8050, debug=True)
