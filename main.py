import os
import sys
from asyncio import sleep

import discord
from discord.ext import commands, tasks

from live import live

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = 'M>', help_command = None, intents = intents)

token = os.environ['token']

# Start of Bot

@client.event
async def on_ready():
	status = discord.Activity(name = "netstat", type = 3)
	await client.change_presence(activity = status)
		
	print("yey")
  
@client.command()
async def test(ctx):
 	await ctx.send(ctx.guild.member_count)
  
# End of Bot

live()
client.run(token)
