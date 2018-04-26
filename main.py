import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Nixeus, a Discord Bot')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("\n")

@bot.command()
async def chart(ctx, ticker: str, time: str):
    await ctx.send(ticker + " " + time)

bot.run('MzAwNDkzODY2MjY2NTI1Njk2.DcKn8g.nnGuJDJYq56vi11bVz--GEal3MA')