import os
import sys
import urllib.parse
from asyncio import sleep

import discord
from discord.ext import commands, tasks

from live import live

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = 'm>', help_command = None, intents = intents)

token = os.environ['token']

# Start of Bot

@client.event
async def on_ready():
	status = discord.Activity(name = "Mathematics", type = 3)
	await client.change_presence(activity = status)
		
	print("yey")
  
@client.command()
async def wa(ctx, *, arg):
  result = "https://www.wolframalpha.com/input/?i=" + urllib.parse.quote(arg)
  await ctx.send(result)
  
# End of Bot

live()
client.run(token)
