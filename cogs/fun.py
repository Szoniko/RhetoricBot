import discord
import config
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Fun(commands.Cog):

    # initialize
    def __init__(self, client):
        self.client = client

    # confirm that cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'fun' loaded")

    """USE THE DECORATOR @commands.command INSTEAD OF @client.command"""

    @cog_ext.cog_slash(name="imannoyed")
    async def imannoyed(self, ctx: SlashContext):
        await ctx.send("why are you annoyed?")

    @cog_ext.cog_slash(name="hentai")
    async def hentai(self, ctx: SlashContext):
        await ctx.send("`https://bit.ly/2KAOWap`")

    @cog_ext.cog_slash(name="Dont-call-me-a-furry")
    async def callmeafurryonemoretime(self, ctx: SlashContext):
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
