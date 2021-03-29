import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
import praw
import config
import os

client: Bot = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("ready")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    join_responses = []
    await channel.send(f'{random.choice(join_responses)}'
    
@client.event
async def on_member_leave(member):
    channel = discord.utils.get(member.guild.text_channels, name="goodbye")
    leave_responses = []
    await channel.send(f'{random.choice(leave_responses)}'

##################################################

@client.command()
async def ping(ctx):
    ctx.send("pong")


if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith("py"):
            extension = file[:-3]
            try:
                client.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension '{extension}'\n{exception}")

client.run(config.auth)
