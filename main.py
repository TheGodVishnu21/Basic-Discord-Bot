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

# Command to respond with a greeting
@bot.command(name='hello', help='Responds with a greeting')
async def hello(ctx):
    await ctx.send('Hello! I am a bot of The God Empire, bestowed with intents!')

# Replace 'your_token_here' with the actual token.
bot.run('your_token_here')
