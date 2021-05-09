from utils.hypixelUtils import HypixelUtils as hu
import discord, config
from discord.ext import commands

class HypixelCommands(commands.Cog):

    #initialize 
    def __init__(self, client):
        self.client = client

    #confirm that cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'HypixelCommands' loaded")

    """USE THE DECORATOR @commands.command INSTEAD OF @client.command"""

    @commands.command()
    async def weekly(self, ctx):
        await ctx.send("Thinking...")
        embed = hu.get_members_gexp(config.guild_name)
        await ctx.send(embed=embed)

    @commands.command()
    async def weeklyp(self, ctx, player):
        embed = hu.get_player_gexp(player)
        await ctx.send(embed=embed)

# don't touch this
def setup(client):
    client.add_cog(HypixelCommands(client))
    