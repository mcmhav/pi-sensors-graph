import os
import pandas as pd
import matplotlib.pyplot as plt

from plotly import tools
import plotly.offline as py_offline
import plotly.graph_objs as go
import plotly.plotly as py

def make_dir(dir='plots'):
    if not os.path.exists(dir):
        os.mkdir(dir)

def plot_df(df, path):
    df['epoch'] = pd.to_datetime(
        df['epoch'], unit='ms', utc=True
    )

    df.plot(x='epoch', figsize=(15, 15))
    plt.savefig('plots/' + path + ".png")
    plt.close()


def plotly_df(df, filename='plots/test.html'):
    make_dir()

    py_offline.plot([{
        'x': df.index,
        'y': df[col],
        'name': col
    } for col in df.columns], filename=filename, auto_open=True)


def plotly_df_multi(df, df2, filename='plots/test.html'):
    # https://plot.ly/python/time-series/
    # https://plot.ly/python/subplots/
    fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)

    traces1 = [go.Scatter(
        x=df.index,
        y=df[col],
        name=col
    ) for col in df.columns]

    traces2 = [go.Scatter(
        x=df2.index,
        y=df2[col],
        mode='markers+text',
        name=col
    ) for col in df2.columns]

    # trace1 = go.Scatter([{
    #     'x': df.index,
    #     'y': df[col],
    #     'name': col
    # } for col in df.columns])

    # trace2 = go.Scatter([{
    #     'x': df2.index,
    #     'y': df2[col],
    #     'name': col
    # } for col in df2.columns])

    traces1_positions = [1] * len(traces1)
    fig.add_traces(traces1, traces1_positions, traces1_positions)

    traces1_positions_col = [1] * len(traces2)
    traces1_positions_row = [2] * len(traces2)
    fig.add_traces(traces2, traces1_positions_row, traces1_positions_col)

    layout = go.Layout(
        yaxis=dict(
            domain=[0, 0.8],
        ),
        yaxis2=dict(
            domain=[0.9, 1],
        ),
    )

    # fig['layout'].update()
    fig.update(layout=layout)

    py_offline.plot(fig, filename=filename, auto_open=True)

