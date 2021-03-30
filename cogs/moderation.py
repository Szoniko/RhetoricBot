import discord, config
from discord.ext.commands.errors import MissingPermissions
from discord.ext import commands


class Moderation(commands.Cog):

    #initialize 
    def __init__(self, client):
        self.client = client

    #confirm that cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'Moderation' loaded")



    """USE THE DECORATOR @commands.command INSTEAD OF @client.command"""


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason):
        try:
            if reason is not None:
                member.kick(reason=reason)
            else:
                member.kick()
            ctx.send(f"{member} was kicked by **{ctx.message.author}**.\n**REASON**: {reason}")
        except MissingPermissions:
            ctx.send("You can't do that silly! *missing permissions*")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member):
        try:
            member.ban()
            ctx.send(f"{member} was banned by **{ctx.message.author}**.")
        except MissingPermissions:
            ctx.send("You can't do that silly! *missing permissions*")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member, reason):
        try:
            if reason is not None:
                member.unban(reason=reason)
            else:
                member.unban()
            ctx.send(f"{member} was unbaned by **{ctx.message.author}**.\n**REASON**: {reason}")
        except MissingPermissions:
            ctx.send("You can't do that silly! *missing permissions*")


# don't touch this
def setup(client):
    client.add_cog(Moderation(client))
