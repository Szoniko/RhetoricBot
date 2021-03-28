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
async def winners(ctx):
    list = ["saffire",
            "oMilan",
            "V2H",
            "MarenoIMopeMope",
            "bentobox",
            "pierrsch",
            "Wolvez774",
            "PlayerOfTheRoom",
            "bread",
            "OhZak",
            "Shadowflame5998",
            "Ghostofyaboi",
            "Lewpick36",
            "Rytherum",
            "Szoniko",
            "MaksiuPogChamp",
            "MathyNL",
            "dikkie",
            "complainment",
            "krypt1k187",
            "YoYoYoZ",
            "Mytholicle",
            "taco gaming",
            "Magenta_cloud",
            "killerishere078",
            "SwiftRabbit2619",
            "b0bd0g",
            "OxygenProxygen",
            "Cyberlogical",
            "simptoretet0"]
    random.shuffle(list)
    for i in range(0, 5):
        await ctx.send(list[i])


client.run(auth)