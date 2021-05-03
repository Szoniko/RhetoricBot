import discord, config
from discord.ext import commands


class CommandErrorHandler(commands.Cog):

    #initialize 
    def __init__(self, client):
        self.client = client

    #confirm that cog loaded, edit only the name of the cog
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'command_error_handler' loaded")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Now, I know this is a mess of elifs
        # but when we are coding this
        # python 3.10 isn't out yet
        # so we can't use match
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error! `MissingRequiredArgument`.")
        elif isinstance(error,  commands.MissingPermissions):
            await ctx.send("Error! You can't do that silly!\n*missing permissions*")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Error! `BadArgument`.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Error! `CommandNotFound`.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("Error! `DisabledCommand`.")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send("Error! `TooManyArguments`.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Error! `CommandOnCooldown`.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Error! `MemberNotFound`.")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send("Error! `ChannelNotFound`.")
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send("Error! `RoleNotFound`.")
        elif isinstance(error, commands.EmojiNotFound):
            await ctx.send("Error! `EmojiNotFound`.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Error! `CheckFailure`.")
        elif isinstance(error, commands.ExtensionError):
            await ctx.send("Error! `ExtensionError`.")
        else:
            await ctx.send(f"Unhandled error! Please contact your administrator about this!\n{error}")
# don't touch this
def setup(client):
    client.add_cog(CommandErrorHandler(client))
