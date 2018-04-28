# import discord
from discord.ext import commands
import sys
import pandas as pd
import plotly as py
import plotly.graph_objs as go

# Set credentials for plotly
py.tools.set_credentials_file(username='smsailer', api_key='ZBEjmKdpZAO1LlfQP3Ca')

# URL for intraday stocks [1min] [5min] [15min] [30min] [60min]
URL_STOCKS_INTRADAY = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="


# Our bot, Nixeus
Nixeus = commands.Bot(command_prefix='!', description='Nixeus, a Discord Bot')


def print_df_info(data_frame):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Data Frame ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(data_frame)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DF Columns ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(data_frame.columns)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DF Values ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print(data_frame.values)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DF Describe ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(data_frame.describe())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DF Types ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(data_frame.dtypes)


#  This helper method uses plotly to create a OHLC chart locally, given a data_frame
def print_ohlc_chart(data_frame):
    trace = go.Ohlc(x=data_frame['timestamp'],
                    open=data_frame['open'],
                    high=data_frame['high'],
                    low=data_frame['low'],
                    close=data_frame['close'])

    layout = go.Layout(
        xaxis=dict(
            rangeslider=dict(
                visible=False
            )
        )
    )

    data = [trace]

    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='OHLC without Rangeslider')


@Nixeus.event
async def on_ready():
    print('Logged in as')
    print(Nixeus.user.name)
    print(Nixeus.user.id)
    print("\n")


@Nixeus.command()
async def chart(ctx, ticker: str, time: str):

    url = URL_STOCKS_INTRADAY + ticker + "&interval=" + time.__str__() + "&apikey=JDXPDDU9XXF3GIHD"

    data_frame = pd.read_csv(url + "&datatype=csv")
    print_df_info(data_frame)
    print_ohlc_chart(data_frame)
    sys.stdout.flush()  # Force a buffer flush in console


# Active our bot, .run({secret token})
Nixeus.run('MzAwNDkzODY2MjY2NTI1Njk2.DcKn8g.nnGuJDJYq56vi11bVz--GEal3MA')
