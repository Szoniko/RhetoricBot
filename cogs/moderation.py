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
                await member.kick(reason=reason)
            else:
                await member.kick()
            await ctx.send(f"{member} was kicked by **{ctx.message.author}**.\n**REASON**: {reason}")
        except MissingPermissions:
            await ctx.send("You can't do that silly! *missing permissions*")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member):
        try:
            await member.ban()
            await ctx.send(f"{member} was banned by **{ctx.message.author}**.")
        except MissingPermissions:
            await ctx.send("You can't do that silly! *missing permissions*")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member, reason):
        try:
            if reason is not None:
                await member.unban(reason=reason)
            else:
                await member.unban()
            await ctx.send(f"{member} was unbaned by **{ctx.message.author}**.\n**REASON**: {reason}")
        except MissingPermissions:
            await ctx.send("You can't do that silly! *missing permissions*")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member):
        try:
            role = discord.utils.get(member.guild.roles, name="muted")
            await member.add_roles(role)
            await ctx.send(f"{member} was muted by **{ctx.message.author}**")
        except MissingPermissions:
            await ctx.send("You can't do that silly! *missing permissions*")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member):
        try:
            role = discord.utils.get(member.guild.roles, name="muted")
            await member.remove_roles(role)
            await ctx.send(f"{member} was unmuted by {ctx.message.author}")
        except MissingPermissions:
            await ctx.send("You can't do that silly! *missing permissions*")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lock(ctx, channel: discord.channel):
        pass

# don't touch this
def setup(client):
    client.add_cog(Moderation(client))
