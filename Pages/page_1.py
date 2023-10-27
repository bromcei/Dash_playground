from dash import dcc, html
from Pages.Filters.topline_filters import top_line_filter
def DataQualityLayout(data_obj):
    return html.Iframe(src=r'assets/page1.html', style={"frameBorder": "0", "height": "100vh", "width": "100%"})