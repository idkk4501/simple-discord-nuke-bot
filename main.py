import discord
from discord.ext import commands
import asyncio

TOKEN = 'your token'   # replace ts with ur bot token
SPAM = 'your spam message' # replace ts with ur spam message
guild = 'your guild name' # replace with what u want the nuked server to be renamed to

bot = commands.Bot(command_prefix=',' , intents=intents)

@bot.event
async def on_ready():
  print('BOT STARTED SUCCESSFULLY')

