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
        self.df = self.df_org.drop_duplicates(keep="first")
        print(self.df.info)
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

    def get_col_unique_values(self, col):
        return self.df[col].sort_values().unique().tolist()

    def box_plot(self, col_x, year, make, model, transmission, fuel, color):
        print(type(year[0]))
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
        df_graph = self.df[
            (self.df["year"] >= year[0]) &
            (self.df["year"] <= year[1]) &
            (self.df["make"].isin(make)) &
            (self.df["model"].isin(model)) &
            (self.df["transmission"].isin(transmission)) &
            (self.df["fuel"].isin(fuel)) &
            (self.df["color"].isin(color))
            ]
        fig = px.box(df_graph.sort_values(col_x), x=col_x, y="price", log_y=True, template="plotly_white")
        # if col_x == "make":
        #     fig.update_layout(width=3000)
        # if col_x == "model":
        #     fig.update_layout(width=12000)
        # else:
        #     fig.update_layout(width=None)
        return fig

    def line_plot(self):
        pass

