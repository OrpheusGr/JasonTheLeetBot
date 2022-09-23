# Imports
import discord
from discord.ext import commands
import leetdaily

# Credentials
TOKEN = 'Bot token here'

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command()
async def leetcode(ctx):
    x = leetdaily.caller()
    await ctx.send(x)

client.run(TOKEN)
