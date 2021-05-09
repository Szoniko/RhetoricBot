import config
import requests
import discord

class HypixelUtils:
    
    def get_members_gexp(guild):
        g = requests.get("https://api.hypixel.net/guild?key=" + config.HYPIXEL_API_KEY + "&name=" + guild)
        g = g.json()

        embed = discord.Embed(
        title = "People who don't meet the requirements",
        description = '',
        colour = discord.Colour.red()
        )

        for i in range(len(g['guild']['members'])):
            uuid = g['guild']['members'][i]['uuid']

            x = requests.get("https://playerdb.co/api/player/minecraft/" + uuid)
            x = x.json()
            name = x['data']['player']['username']


            
            expHistory = expHistory = g['guild']['members'][i]['expHistory']
            expHistory = sum(expHistory.values())
            

            if (int(expHistory) > config.GXP_REQUIREMENT):
                continue


            expHistory = "{:,}".format(sum(g['guild']['members'][i]['expHistory'].values()))

            embed.add_field(name=f"{name}", value=f"{expHistory} GEXP \n")

        return embed 

    def get_player_uuid_from_ign(name):
        r = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name).json()
        uuid = r['id']
        return uuid


    def get_player_gexp(player):
        uuid = HypixelUtils.get_player_uuid_from_ign(player)
        g = requests.get("https://api.hypixel.net/guild?key=" + config.HYPIXEL_API_KEY + "&name=" + config.guild_name).json()

        embed = discord.Embed(
        title = f"Player GEXP in the last week.",
        description = '',
        )

        for i in range(len(g['guild']['members'])):
            if g['guild']['members'][i]['uuid'] == uuid:
                expHistory = g['guild']['members'][i]['expHistory']
                expHistory = sum(expHistory.values())
                embed.add_field(name=player, value=expHistory)
                if expHistory > config.GXP_REQUIREMENT:
                    embed.colour = discord.Colour.green()
                else:
                    embed.colour = discord.Colour.red()

                return embed