import discord
from discord.ext import commands
from bot_logic import gen_pass, flip_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def passgen(ctx, pass_length = 10):
    await ctx.send(gen_pass(pass_length))

@bot.command()
async def coinflip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("TOKEN DISINI")
