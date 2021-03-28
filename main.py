import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random

auth = "you aint getting it"

client: Bot = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("ready")

##################################################

@client.command()
async def ping(ctx):
    ctx.send("pong")


client.run(auth)
