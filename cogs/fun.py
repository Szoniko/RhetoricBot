import discord
import config
from discord.ext import commands


class Fun(commands.Cog):

    # initialize
    def __init__(self, client):
        self.client = client

    # confirm that cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'fun' loaded")

    """USE THE DECORATOR @commands.command INSTEAD OF @client.command"""

    @commands.command(aliases=["_.", "-.", ".."])
    async def imannoyed(self, ctx):
        await ctx.send("why are you annoyed?")

    @commands.command()
    async def hentai(self, ctx):
        await ctx.send("`https://bit.ly/2KAOWap`")

    @commands.command(aliases=["cmafomt", "imnotafurry"])
    async def callmeafurryonemoretime(self, ctx):
        embed = discord.Embed(
            title="I swear",
            description="If you say it one more goddamn time",
            colour=discord.Colour.magenta()
        )
        embed.add_field(name="Im gonna break your fucking head",
                        value="AAAAAAAAAAAAAAAH")
        await ctx.send(embed=embed)


# don't touch this
def setup(client):
    client.add_cog(Fun(client))
