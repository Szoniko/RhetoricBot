import discord, config
from discord.ext import commands


class Example_class(commands.Cog):

    #initialize 
    def __init__(self, client):
        self.client = client

    #confirm that cog loaded, edit only the name of the cog
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog example-cog loaded")

    #the commands itself, you can delete this one 

    """USE THE DECORATOR @commands.command INSTEAD OF @client.command"""

    @commands.command()
    async def example(self, ctx):
        await ctx.send("example command!")

# don't touch this, just rename "Example_class" to the class name
def setup(client):
    client.add_cog(Example_class(client))
