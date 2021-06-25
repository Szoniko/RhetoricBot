from utils.hypixelUtils import HypixelUtils as hu
import discord
import config
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option


class HypixelCommands(commands.Cog):

    # initialize
    def __init__(self, client):
        self.client = client

    # confirm that cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'HypixelCommands' loaded")

    """USE THE DECORATOR @commands.command INSTEAD OF @client.command"""

    @cog_ext.cog_slash(name="weekly",
                       description="shows weekly gxp",
                       options=[create_option(name="mode",
                                              description="Entire guild or one player?",
                                              option_type=3,
                                              required=True,
                                              choices=["PLAYER", "GUILD"]
                                              ),
                                create_option(name="player",
                                              description="If you chose 'PLAYER', insert his ign",
                                              option_type=3,
                                              required=False
                                              )
                                ]
                       )
    async def weekly(self, ctx: SlashContext, mode: str, player: str = None):
        mode = mode.upper()
        player = player.upper() if player is not None else None
        if mode == "PLAYER":
            await ctx.defer()
            embed = hu.get_player_gexp(player)
            await ctx.send(embed=embed)
        elif mode == "GUILD":
            await ctx.defer()
            embed = hu.get_members_gexp(config.GUILD_NAME)
            await ctx.send(embed=embed)
        else:
            await ctx.send(content="something went wrong, sorry!")


# don't touch this
def setup(client):
    client.add_cog(HypixelCommands(client))
