from discord.ext import commands
from pprint import pprint
import requests
import plotly.plotly as py
import plotly.graph_objs as go

BOT_TOKEN = 'MzAwNDkzODY2MjY2NTI1Njk2.Dmsy6g.Z4OEYFrSI9CSbF-iqHZfnzxs2BY'
ERROR_BASE = 'This command was not recognized or failed to run properly.'
ERROR_FROM_PAIR = '`from_pair` must be a 3 character alphanumeric string (BTC, ETH, ...)'
ERROR_TO_PAIR = '`to_pair` must be a 3 character alphanumeric string (BTC or USD)'
ERROR_TO_PAIR_VALUES = '`to_pair` must be either BTC or USD'
ERROR_CANDLE_SCALE = '`candle_scale` must be of the format <int><str> -- 1min, 1d, 1w, 1m'

CRYPTO_COMPARE_URL = 'https://min-api.cryptocompare.com'

bot = commands.Bot(command_prefix='!', description='Nixeus')

@bot.event
async def on_ready():
    print('Logged in as `' + bot.user.name + '` - id: ' + str(bot.user.id))

# Charts a crypto against an asset (USD or BTC) and returns the png of the chart
# e.g. `!chart BTC USD 1d` charts BTC against USD, using 1d candles
@bot.command()
async def chart(ctx, from_pair: str, to_pair: str, timeframe: str):
    # Ensure validity of from_pair and to_pair
    if(not await validate_pairs(ctx, from_pair.lower().strip(), to_pair.lower().strip())):
        return
    
    # Ensure validity of timeframe
    if(not await validate_timeframe(ctx, timeframe.lower().strip())):
        return
    
    # Get the data
    url = f'{CRYPTO_COMPARE_URL}/data/histoday?fsym={from_pair.upper()}&tsym={to_pair.upper()}&limit=100'
    response = requests.get(url)['Data']
    pprint(response)
    open = (obj.open for obj in response)
    high = (obj.high for obj in response)
    low = (obj.low for obj in response)
    close = (obj.close for obj in response)
    time = (obj.time for obj in response)

    trace = go.Ohlc(x=time,
                    open=open,
                    high=high,
                    low=low,
                    close=close)
    data = [trace]
    py.iplot(data, filename='simple_ohlc')

    return

# Ensures the validity (content & format) of the from_pair and to_pair
# Proper format: from_pair="BTC", to_pair="USD"
async def validate_pairs(ctx, from_pair: str, to_pair: str):
    # Check `from_pair` for length
    if (len(from_pair) is not 3 or not from_pair.isalpha()):
        print(len(from_pair))
        await ctx.send(ERROR_FROM_PAIR)
        return False

    # Check `to_pair` for length
    if (len(to_pair) is not 3 or not to_pair.isalpha()):
        print(len(to_pair))
        await ctx.send(ERROR_TO_PAIR)
        return False

    # `to_pair` must be either USD or BTC 
    if (not to_pair == 'usd' and not to_pair == 'btc'):
        await ctx.send(ERROR_TO_PAIR_VALUES)
        return False

    # All is good, return True
    return True

# Ensures the validity (content & format) of the from_pair and to_pair
# Proper format: from_pair="BTC", to_pair="USD"
async def validate_timeframe(ctx, timeframe: str):
    # Split the timeframe into list of [int, str] value, e.g. 1d -> [1, d]
    
    # For now, only 1d is supported
    if (not timeframe.__eq__('1d')):
        return False
    
    # All is good, return True
    return True

# Run the program
bot.run(BOT_TOKEN)
