import discord
from discord.ext import commands

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Event: New message is received
@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself to prevent infinite loops
    if message.author == bot.user:
        return

    # Process commands
    await bot.process_commands(message)

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Say
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# Run the bot with your bot token
bot.run('YOUR_BOT_TOKEN')
