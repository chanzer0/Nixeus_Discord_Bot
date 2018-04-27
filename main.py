import discord
from discord.ext import commands
import json
import pandas as pd
import matplotlib.pyplot as plt

# URL for intraday stocks [1min] [5min] [15min] [30min] [60min]
URL_stocks_intraday = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="


# Our bot, Nixeus
Nixeus = commands.Bot(command_prefix='!', description='Nixeus, a Discord Bot')


@Nixeus.event
async def on_ready():
    print('Logged in as')
    print(Nixeus.user.name)
    print(Nixeus.user.id)
    print("\n")


@Nixeus.command()
async def chart(ctx, ticker: str, time: str):
    URL = URL_stocks_intraday + ticker + "&interval=" + time + "&apikey=JDXPDDU9XXF3GIHD"
    data_frame = pd.read_csv(URL + "&datatype=csv")
    print(data_frame)


Nixeus.run('MzAwNDkzODY2MjY2NTI1Njk2.DcKn8g.nnGuJDJYq56vi11bVz--GEal3MA')
