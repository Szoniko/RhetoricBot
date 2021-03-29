import discord, config
from discord.ext import commands


class Purge(commands.Cog):

    #initialize
    def __init__(self, client):
        self.client = client

    #confirm that cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print('cog purge is loaded')

    #purge command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(ctx, limit: int):
        try:
            await ctx.channel.purge(limit=limit)
            await ctx.send(f"Chat cleared by {ctx.author.mention}")
            await ctx.message.delete()
        except Exception as e:
            ctx.send("Something went wrong, or you don't have permission to do that!")
            ctx.send(e)
            
def setup(client):
    client.add_cog(Purge(client))