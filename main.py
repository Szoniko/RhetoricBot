import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import config
import os
from discord_slash import SlashCommand 
client: Bot = commands.Bot(command_prefix=config.command_prefix)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    await channel.send(f'{random.choice(config.join_responses)}')

@client.event
async def on_member_leave(member):
    channel = discord.utils.get(member.guild.text_channels, name="goodbye")
    await channel.send(f'{random.choice(config.leave_responses)}')

##################################################

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")


if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.startswith("--"):
            continue
        if file.endswith("py"):
            extension = file[:-3]
            try:
                client.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension '{extension}'\n{exception}")

client.run(config.auth)
