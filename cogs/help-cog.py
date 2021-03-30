import discord, config
from discord.ext import commands


class Help(commands.Cog):

    #initialize 
    def __init__(self, client):
        self.client = client

    #confirm that cog loaded, edit only the name of the cog
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'Help' loaded")

    #the command itself

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Commands',
            description = '',
            colour = discord.Colour.green()
        )
        # You can edit the text or name stuff
        embed.set_footer(text='https://github.com/Szoniko/RhetoricBot')
        embed.add_field(name='.help', value='Sends this embed')
        # Just add "embed.add_field(name='.COMMAND'), value='DESCRIPTION'" to add more fields

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))