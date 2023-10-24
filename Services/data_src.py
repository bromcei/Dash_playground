import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import time
from datetime import date, datetime, timedelta
import os


class DataProcessor():
    def __init__(self):
        self.url = 'https://drive.google.com/file/d/1TDSVowlbRnB6rs9mEd7jLaVjFYvhRvIN/view?usp=sharing'
        self.url = 'https://drive.google.com/uc?id=' + self.url.split('/')[-2]
        self.df_org = pd.read_csv(r"Data/carvertical.csv", index_col=[0], sep=";")
        self.df = self.df_org.drop_duplicates(keep="first").copy()
        self.df_analysis = self.df.dropna().copy()
        self.makes = self.df["make"].unique()
        self.models = self.df["model"].unique()
        self.trans = self.df["transmission"].unique()
        self.fuels = self.df["fuel"].unique()
        self.colors = self.df["color"].unique()

    def return_nulls_col(self, column):
        null_cols = [col for col in self.df.columns if col != column]
        df_nuls = self.df[null_cols].isnull().groupby([self.df[column]]).sum().reset_index()
        nans_sum = df_nuls[null_cols].sum(axis=1)
        df_nuls['total_nuls'] = nans_sum
        return df_nuls.sort_values('total_nuls', ascending=False)

    def get_columns(self, exlude=None):
        if exlude is None:
            return self.df.columns
        else:
            return [col for col in self.df.columns if col not in exlude]

    def get_year_range(self):
        year_min = np.min(self.df["year"])
        year_max = np.max(self.df["year"])
        return [int(year_min), int(year_max)]

    def get_col_unique_values(self, col):
        return self.df[col].sort_values().unique().tolist()

    def apply_filter(self, year, make, model, transmission, fuel, color):
        if len(make) == 0:
            make = self.makes
        if len(model) == 0:
            model = self.models
        if len(transmission) == 0:
            transmission = self.trans
        if len(fuel) == 0:
            fuel = self.fuels
        if len(color) == 0:
            color = self.colors
        df_filtered = self.df[
            (self.df["year"] >= year[0]) &
            (self.df["year"] <= year[1]) &
            (self.df["make"].isin(make)) &
            (self.df["model"].isin(model)) &
            (self.df["transmission"].isin(transmission)) &
            (self.df["fuel"].isin(fuel)) &
            (self.df["color"].isin(color))
            ].copy()
        return df_filtered

    def apply_filter_with_q(self, q_low, q_high, year, make, model, transmission, fuel, color):
        if len(make) == 0:
            make = self.makes
        if len(model) == 0:
            model = self.models
        if len(transmission) == 0:
            transmission = self.trans
        if len(fuel) == 0:
            fuel = self.fuels
        if len(color) == 0:
            color = self.colors

        q_lower = self.df_analysis["price"].quantile(q_low)
        q_higher = self.df_analysis["price"].quantile(q_high)
        df_filtered = self.df_analysis[
            (self.df_analysis["price"] >= q_lower) &
            (self.df_analysis["price"] <= q_higher) &
            (self.df_analysis["year"] >= year[0]) &
            (self.df_analysis["year"] <= year[1]) &
            (self.df_analysis["make"].isin(make)) &
            (self.df_analysis["model"].isin(model)) &
            (self.df_analysis["transmission"].isin(transmission)) &
            (self.df_analysis["fuel"].isin(fuel)) &
            (self.df_analysis["color"].isin(color))
            ].copy()
        return df_filtered

    def box_plot_ov(self, col_x, year, make, model, transmission, fuel, color):
        df_graph = self.apply_filter(year, make, model, transmission, fuel, color)
        fig = px.box(df_graph.sort_values(col_x), x=col_x, y="price", log_y=True, template="plotly_white")
        # if col_x == "make":
        #     fig.update_layout(width=3000)
        # if col_x == "model":
        #     fig.update_layout(width=12000)
        # else:
        #     fig.update_layout(width=None)
        return fig

    def bar_line_chart_ov(self, year, make, model, transmission, fuel, color):
        df_graph = self.apply_filter(year, make, model, transmission, fuel, color)
        df_graph = df_graph.groupby("year").agg(
            {"price": ["mean"], "make": ["count"], "model": [lambda x: x.nunique()]}).reset_index().droplevel(1, axis=1)
        fig = px.line(x=df_graph["year"], y=df_graph["price"], color=px.Constant("Average Price"),
                      labels=dict(x="year", y="Average Price"), template="plotly_white")
        fig.update_layout(
            yaxis2=dict(
                title="Vehicle Count",
                # overlaying='y',
                side='right'
            ),
            yaxis1 = dict(
                title="Average Price",
                overlaying='y2',
                side='left'
            )
        )
        fig.add_bar(x=df_graph["year"], y=df_graph["make"], name="Vehicle Count", yaxis="y2")
        # fig.update_layout(traceorder="reversed")
        return fig


    def hist_plot(self, year, make, model, transmission, fuel, color, quantile_range, category_name, category_value_1, category_value_2):
        df_filtered = self.apply_filter_with_q(quantile_range[0], quantile_range[1], year, make, model, transmission,
                                               fuel, color)

        cat_1_prices = df_filtered[df_filtered[category_name] == category_value_1]["price"].to_numpy()
        cat_2_prices = df_filtered[df_filtered[category_name] == category_value_2]["price"].to_numpy()

        df_hist = pd.DataFrame(dict(
            series=np.concatenate(([category_value_1] * len(cat_1_prices), [category_value_2] * len(cat_2_prices))),
            data=np.concatenate((cat_1_prices, cat_2_prices))
        ))
        fig = px.histogram(df_hist, x="data", color="series", barmode="overlay", nbins=20)
        return fig

