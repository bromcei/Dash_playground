import dash
import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
# from datetime import date, datetime, timedelta



def box_plot(df, col_x):
    fig = px.box(df, x=col_x, y="price", log_y=True, template="plotly_white")
    return fig

def telemetryV3_live_stream():
    fig = px.line(
        V3().live_data_stream(),
        x='date_bin',
        y='data_sets',
        color='chart_label',
        color_discrete_map={
            "parsed_data": "green",
            "unparsed_data": "#C42200"
        }
    )
    fig.update_xaxes(title_text=None)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_layout(
        showlegend=True,
        font_color="white",
        legend_font_color="white",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        legend_title_text=None,
        margin=dict(t=10, l=10, b=10, r=10),
        xaxis=dict(
            autorange=True,
            showgrid=False,
            ticks='',
            showticklabels=True,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig


def telemetryWika_live_stream():
    fig = px.line(
        Wika().live_data_stream(),
        x='date_bin',
        y='data_sets',
        color='chart_label',
        color_discrete_map={
            "parsed_data": "green",
            "unparsed_data": "#C42200"
        }
    )
    fig.update_xaxes(title_text=None)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_layout(
        showlegend=True,
        font_color="white",
        legend_font_color="white",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        legend_title_text=None,
        margin=dict(t=10, l=10, b=10, r=10),
        xaxis=dict(
            autorange=True,
            showgrid=False,
            ticks='',
            showticklabels=True,
        ),
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)"
    )
    return fig


def erx_fig(n_months=4):
    df_rx = Heap().rxs_data(n_months)
    fig = px.bar(df_rx, x='date', y='rxs_count', text_auto='.3s', title=None)
    fig.update_traces(textfont_size=16, textangle=0, textposition="outside")
    fig.update_xaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray', title=None)
    fig.update_yaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray')

    fig.update_traces(marker_color='#69480A')
    fig.update_layout(
        font_family='Segoe UI Light',
        font_color="white",
        yaxis_range=[0, int(np.max(df_rx['rxs_count']) * 1.25)],
        showlegend=False,
        height=250,
        # xaxis_title="Date",
        yaxis_title="eRx",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=5,
            r=5,
            b=5,
            t=5,
            pad=5
        )
    )
    try:
        last_recipe_date = np.max(df_rx[df_rx['rxs_count'] != 0]['date']).strftime("%Y-%m-%d")
    except ValueError:
        last_recipe_date = 'No Data!!!'

    if last_recipe_date is None:
        last_recipe_date = 'NO DATA'
    return fig, last_recipe_date


def visits_fig(n_months=4):
    df_visits = Heap().visits_data(n_months)
    fig = px.bar(x=df_visits['date'], y=df_visits['visit_count'], text_auto='.3s', title=None)
    fig.update_traces(marker_color='#106669')
    fig.update_traces(textfont_size=16, textangle=0, textposition="outside")
    fig.update_xaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray', title=None)
    fig.update_yaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray')
    fig.update_layout(
        font_family='Segoe UI Light',
        font_color="white",
        yaxis_range=[0, int(np.max(df_visits['visit_count']) * 1.25)],
        showlegend=False,
        height=250,
        # xaxis_title="Date",
        yaxis_title="Visits",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=5,
            r=5,
            b=5,
            t=5,
            pad=5
        )
    )
    try:
        last_visit_date = np.max(df_visits[df_visits['visit_count'] != 0]['date']).strftime("%Y-%m-%d")
    except ValueError:
        last_visit_date = 'No Data!!!'

    return fig, last_visit_date

def missing_spec():
    return Heap().return_no_of_missing_spec()

def missing_hcps():
    return Heap().return_no_of_missing_hcps()

def missing_spec_line_plot():
    df = Heap().missing_spec_by_date()
    fig = px.line(x=df['yyyy_mm'], y=df['count_data'], title=None)
    fig.update_traces(line_color='green', line_width=5)
    fig.update_xaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray', title=None)
    fig.update_yaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray')
    fig.update_layout(
        font_family='Segoe UI Light',
        font_color="white",
        yaxis_range=[0, int(np.max(df['count_data']) * 1.25)],
        showlegend=False,
        height=250,
        # xaxis_title="Date",
        yaxis_title="No of Docs",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(
            l=5,
            r=5,
            b=5,
            t=35,
            pad=5
        )
    )
    return fig

def missing_hcp_line_plot():
    df = Heap().missing_hcps_by_date()
    fig = px.line(x=df['yyyy_mm'], y=df['count_data'], title=None)
    fig.update_traces(line_color='green', line_width=5)
    fig.update_xaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray', title=None)
    fig.update_yaxes(showgrid=True, linewidth=1.5, linecolor='#8D95A2', gridcolor='gray')
    fig.update_layout(
        font_family='Segoe UI Light',
        font_color="white",
        yaxis_range=[0, int(np.max(df['count_data']) * 1.25)],
        showlegend=False,
        height=250,
        # xaxis_title="Date",
        yaxis_title="No of Hcps",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(
            l=5,
            r=5,
            b=5,
            t=35,
            pad=5
        )
    )
    return fig
