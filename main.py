import discord
from discord.ext import commands

# Define the intents that we need
intents = discord.Intents.default()
intents.messages = True  # For receiving messages
intents.guilds = True    # For server-specific commands

# The bot initialization with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Replace 'your_token_here' with the actual token.
bot.run('your_token_here')
