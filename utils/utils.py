# Proudly stolen
# from a github repo
# https://github.com/Smudge-Studios/HypixelBot/blob/main/utils/utils.py
# thanks, smudge studios
import config
import datetime
from datetime import datetime
import re
from aiohttp import ClientSession

API_KEY = config.HYPIXEL_API_KEY
    

class con:
    def log(text: str):
        now = datetime.now()
        time = now.strftime("%m/%d/%Y %H:%M")
        with open('utils\\logs\\bot.log', 'a') as logfile:
            logfile.write(f"{time}: {text}\n\n")
        print(f"{time}: {text}")

    def start():
        now = datetime.now()
        time = now.strftime("%m/%d/%Y %H:%M")
        with open('utils\\logs\\bot.log', 'a') as logfile:
            logfile.write(f"==========(BOT RESTART AT {time})==========\n")
        with open('utils\\logs\\error.log', 'a') as logfile:
            logfile.write(f"==========(BOT RESTART AT {time})==========\n")

    def wipelogs():
        with open('utils\\logs\\bot.log', 'w'):
            pass

    def wipeerrors():
        with open('utils\\logs\\error.log', 'w'):
            pass


class utils:
    def comma(self, num) -> str:
        """Add comma to every 3rd digit. Takes int or float and
        returns string."""
        if type(num) == int:
            return '{:,}'.format(num)
        elif type(num) == float:
            return '{:,.2f}'.format(num)  # Rounds to 2 decimal places
        elif type(num) == str:
            return num
        else:
            return None

    def guildlevel(self, xp: int):
        """ Return a guild's level from XP. """
        req_exp = [100000,
                   150000,
                   250000,
                   500000,
                   750000,
                   1000000,
                   1250000,
                   1500000,
                   2000000,
                   2500000,
                   2500000,
                   2500000,
                   2500000,
                   2500000,
                   3000000]
        lvl = 0
        for i in range(1000):
            needed = 0
            if i >= len(req_exp):
                needed = req_exp[len(req_exp) - 1]
            else:
                needed = req_exp[i]
            xp -= needed
            if xp < 0:
                return int(lvl)
            else:
                lvl += 1
        return 'N/A'

    def gameconverter(self, game: str) -> str:
        """ Convert a Hypixel game to a readable format. """
        if game == "QUAKECRAFT":
            game = "Quake"
        elif game == "WALLS":
            game = 'Walls'
        elif game == 'PAINTBALL':
            game = 'paintball'
        elif game == 'SURVIVAL_GAMES':
            game = 'Blitz Survival Games'
        elif game == 'TNTGAMES':
            game = 'TNT Games'
        elif game == 'VAMPIREZ':
            game = 'VampireZ'
        elif game == 'WALLS3':
            game = 'Mega Walls'
        elif game == 'ARCADE':
            game = 'Arcade'
        elif game == 'ARENA':
            game = 'Arena'
        elif game == 'UHC':
            game = 'UHC Champions'
        elif game == 'MCGO':
            game = 'Cops and Crims'
        elif game == 'BATTLEGROUND':
            game = 'Warlords'
        elif game == 'SUPER_SMASH':
            game = 'Smash Heroes'
        elif game == 'GINGERBREAD':
            game = 'Turbo Kart Racers'
        elif game == 'HOUSING':
            game = 'Housing'
        elif game == 'SKYWARS':
            game = 'Skywars'
        elif game == 'TRUE_COMBAT':
            game = 'Crazy Walls'
        elif game == 'SPEED_UHC':
            game = 'Speed UHC'
        elif game == 'SKYCLASH':
            game = 'SkyClash'
        elif game == 'LEGACY':
            game = 'Classic Games'
        elif game == 'PROTOTYPE':
            game = 'Prototype'
        elif game == 'BEDWARS':
            game = 'BedWars'
        elif game == 'MURDER_MYSTERY':
            game = 'Murder Mystery'
        elif game == 'BUILD_BATTLE':
            game = 'Build Battle'
        elif game == 'DUELS':
            game = 'Duels'
        elif game == 'SKYBLOCK':
            game = 'Skyblock'
        elif game == 'PIT':
            game = 'The Pit'
        else:
            game = 'N/A'
        return game

    def idtogameconverter(self, game: int) -> str:
        if game == 2:
            game = 'Quake'
        elif game == 3:
            game = 'Walls'
        elif game == 4:
            game = 'Paintball'
        elif game == 5:
            game = 'Blitz Survival Games'
        elif game == 6:
            game = 'TNT Games'
        elif game == 7:
            game = 'VampireZ'
        elif game == 13:
            game = 'Mega Walls'
        elif game == 14:
            game = 'Arcade'
        elif game == 17:
            game = 'Arena'
        elif game == 20:
            game = 'UHC Champions'
        elif game == 21:
            game = 'Cops and Crims'
        elif game == 23:
            game = 'Warlords'
        elif game == 24:
            game = 'Smash Heroes'
        elif game == 25:
            game = 'Turbo Kart Racers'
        elif game == 26:
            game = 'Housing'
        elif game == 51:
            game = 'Skywars'
        elif game == 52:
            game = 'Crazy Walls'
        elif game == 54:
            game = 'Speed UHC'
        elif game == 55:
            game = 'SkyClash'
        elif game == 56:
            game = 'Classic Games'
        elif game == 57:
            game = 'Prototype'
        elif game == 58:
            game = 'BedWars'
        elif game == 59:
            game = 'Murder Mystery'
        elif game == 60:
            game = 'Build Battle'
        elif game == 61:
            game = 'Duels'
        elif game == 63:
            game = 'Skyblock'
        elif game == 64:
            game = 'The Pit'
        return game

    def gameidconverter(self, game: str) -> int:
        game = game.lower()
        game = game.replace('_', ' ')
        if game == 'quake':
            game = 2
        elif game == 'walls':
            game = 3
        elif game == 'paintball':
            game = 4
        elif game == 'blitz survival games':
            game = 5
        elif game == 'vampirez':
            game = 6
        elif game == 'tnt games':
            game = 7
        elif game == 'mega walls':
            game = 13
        elif game == 'arcade':
            game = 14
        elif game == 'arena':
            game = 17
        elif game == 'uhc':
            game = 20
        elif game == 'cops and crims':
            game = 21
        elif game == 'warlords':
            game = 23
        elif game == 'smash heroes':
            game = 24
        elif game == 'turbo kart racers':
            game = 25
        elif game == 'housing':
            game = 26
        elif game == 'skywars':
            game = 51
        elif game == 'crazy walls':
            game = 52
        elif game == 'speed uhc':
            game = 54
        elif game == 'skyclash':
            game = 55
        elif game == 'classic games':
            game = 56
        elif game == 'prototype':
            game = 57
        elif game == 'bedwars':
            game = 58
        elif game == 'murder mystery':
            game = 59
        elif game == 'build battle':
            game = 60
        elif game == 'duels':
            game = 61
        elif game == 'skyblock':
            game = 63
        elif game == 'pit':
            game = 64
        else:
            raise ValueError
        return game

    def timeconverter(self, login: int, logout: int) -> str:
        """ Converts Hypixel login/out time to the appropriate format. """
        try:
            status = 'N/A'
            if login > logout:
                status = 'Online'
            elif login < logout:
                time = datetime.fromtimestamp(logout / 1000.0)
                date = time.strftime("%m/%d/%Y")
                status = 'Offline - Last seen on ' + str(date)
            return status
        except:
            return 'N/A'

    def networklevel(self, exp: int):
        """ Gets a user's Network level from their network xp. """
        try:
            network_level = (((2 * exp) + 30625) ** (1 / 2) / 50) - 2.5
            level = round(network_level, 0)
            return int(level)
        except:
            return 'N/A'

    def getSkillLevel(self, xp: float) -> str:
        prog_req_xp = [50,
                       125,
                       200,
                       300,
                       500,
                       750,
                       1000,
                       1500,
                       2000,
                       3500,
                       5000,
                       7500,
                       10000,
                       15000,
                       20000,
                       30000,
                       50000,
                       75000,
                       100000,
                       200000,
                       300000,
                       400000,
                       500000,
                       600000,
                       700000,
                       800000,
                       900000,
                       1000000,
                       1100000,
                       1200000,
                       1300000,
                       1400000,
                       1500000,
                       1600000,
                       1700000,
                       1800000,
                       1900000,
                       2000000,
                       2100000,
                       2200000,
                       2300000,
                       2400000,
                       2500000,
                       2600000,
                       2750000,
                       2900000,
                       3100000,
                       3400000,
                       3700000,
                       4000000]
        lvl = 0
        rexp = xp
        lievel = 50
        for level in prog_req_xp:
            if rexp >= level:
                rexp -= level
                lvl += 1
                pass
            elif rexp < level:
                lievel = level
                break
        progress = f"{self.comma(int(round(rexp, 0)))}/{self.comma(lievel)}"
        return f"Level {self.comma(lvl)} - {progress} XP"

    def getSkillLevelNumber(self, xp: float) -> int:
        prog_req_xp = [50,
                       125,
                       200,
                       300,
                       500,
                       750,
                       1000,
                       1500,
                       2000,
                       3500,
                       5000,
                       7500,
                       10000,
                       15000,
                       20000,
                       30000,
                       50000,
                       75000,
                       100000,
                       200000,
                       300000,
                       400000,
                       500000,
                       600000,
                       700000,
                       800000,
                       900000,
                       1000000,
                       1100000,
                       1200000,
                       1300000,
                       1400000,
                       1500000,
                       1600000,
                       1700000,
                       1800000,
                       1900000,
                       2000000,
                       2100000,
                       2200000,
                       2300000,
                       2400000,
                       2500000,
                       2600000,
                       2750000,
                       2900000,
                       3100000,
                       3400000,
                       3700000,
                       4000000]
        lvl = 0
        rexp = xp
        for level in prog_req_xp:
            if rexp >= level:
                rexp -= level
                lvl += 1
                pass
            elif rexp < level:
                break
        return lvl

    def getRuneCraftLevel(self, xp: float) -> str:
        prog_req_xp = [50,
                       100, 
                       125,
                       160,
                       200,
                       250,
                       315,
                       400,
                       500,
                       625,
                       785,
                       1000, 
                       1250, 
                       1600, 
                       2000, 
                       2465, 
                       3125,  
                       4000,
                       5000, 
                       6200, 
                       7800, 
                       9800, 
                       12200,
                       15300]
        lvl = 0
        rexp = xp
        lievel = 50
        for level in prog_req_xp:
            if rexp >= level:
                rexp -= level
                lvl += 1
                pass
            elif rexp < level:
                lievel = level
                break
        progress = f"{self.comma(int(round(rexp, 0)))}/{self.comma(lievel)}"
        return f"Level {self.comma(lvl)} - {progress} XP"

    def translateIDName(self, id: str, reverse: bool = False):
        with open('utils/idfile.txt', 'r') as file:
            content = file.read()
        translations = content.split('\n')
        id = id.lower()
        for translation in translations:
            t = translation.split('==')
            print(t)
            if reverse:
                if t[1].lower() == id:
                    return t[0]
            if not reverse:
                if t[0].lower() == id:
                    return t[1]
        return id

    def farmingCollection(self, data: dict):
        collections = ['WHEAT',
                       'CARROT_ITEM',
                       'POTATO_ITEM',
                       'PUMPKIN',
                       'MELON',
                       'SEEDS',
                       'MUSHROOM_COLLECTION',
                       'INK_SACK:3',
                       'CACTUS',
                       'SUGAR_CANE',
                       'FEATHER',
                       'LEATHER',
                       'PORK',
                       'RAW_CHICKEN',
                       'MUTTON',
                       'RABBIT',
                       'NETHER_STALK']
        message = ''
        maxed = 0
        for collection in collections:
            if collection == 'WHEAT':
                req_xp = [50,
                        100,
                        250,
                        500,
                        1000,
                        2500,
                        10000,
                        15000,
                        25000,
                        50000]
            elif collection == 'CARROT_ITEM' or collection == 'POTATO_ITEM':
                req_xp = [100,
                        250,
                        500,
                        1750,
                        5000,
                        10000,
                        25000,
                        50000,
                        100000]
            elif collection == 'PUMPKIN':
                req_xp = [40, 
                        100, 
                        250, 
                        1000, 
                        2500, 
                        5000, 
                        10000, 
                        25000, 
                        50000]
            elif collection == 'MELON':
                req_xp = [250,
                        500,
                        1200,
                        5000,
                        15500,
                        25000,
                        50000,
                        100000,
                        250000]
            elif collection == 'SEEDS':
                req_xp = [50, 
                        100, 
                        250, 
                        1000, 
                        2500, 
                        5000]
            elif collection == 'MUSHROOM_COLLECTION':
                req_xp = [50,
                        100,
                        250,
                        1000,
                        2500,
                        5000,
                        10000,
                        25000,
                        50000]
            elif collection == 'INK_SACK:3':
                req_xp = [75, 
                        200, 
                        500, 
                        2000, 
                        5000, 
                        10000, 
                        20000, 
                        50000, 
                        100000]
            elif collection == 'CACTUS':
                req_xp = [100,
                        250,
                        500,
                        1000,
                        2500,
                        5000,
                        10000,
                        25000,
                        50000]
            elif collection == 'SUGAR_CANE':
                req_xp = [100,
                        250,
                        500,
                        1000,
                        2000,
                        5000,
                        10000,
                        20000,
                        50000]
            elif collection == 'FEATHER':
                req_xp = [50, 
                        100, 
                        250, 
                        1000, 
                        2500, 
                        5000, 
                        10000, 
                        25000, 
                        50000]
            elif collection == 'LEATHER':
                req_xp = [50,
                        100,
                        250,
                        1000,
                        2500,
                        5000,
                        10000,
                        25000,
                        50000,
                        100000]
            elif collection == 'PORK':
                req_xp = [50,
                        100,
                        250,
                        1,000,
                        2,500,
                        5,000,
                        10,000,
                        25,000,
                        50,000]
            elif collection == 'RAW_CHICKEN':
                req_xp = [50,
                        100,
                        250,
                        1000,
                        2500,
                        5000,
                        10000,
                        25000,
                        50000]
            elif collection == 'MUTTON':
                req_xp = [50,
                        100,
                        250,
                        1000,
                        2500,
                        5000,
                        10000,
                        25000,
                        50000]
            elif collection == 'RABBIT':
                req_xp = [50,
                        100,
                        250,
                        1000,
                        2500,
                        5000,
                        10000,
                        25000,
                        50000]
            elif collection == 'NETHER_STALK':
                req_xp = [50,
                    100,
                    250,
                    1000,
                    2500,
                    5000,
                    10000,
                    25000,
                    50000,
                    75000,
                    100000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = self.translateIDName(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        msg = f"{col}: Level {self.comma(lvl)} - MAX\n"
                        maxed += 1
                    else:
                        progress = f"{self.comma(int(round(amount, 0)))}/{self.comma(next_lvl)}"
                        msg = f"{col}: Level {self.comma(lvl)} - {progress} Items\n"
                else:
                    progress = f"0/{self.comma(req_xp[0])}"
                    msg = f"{col}: Level 0 - {progress} Items\n"
                message += msg
        return maxed, len(collections), message

    def miningCollection(self, data: dict):
        collections = ['COBBLESTONE',
                       'COAL',
                       'IRON_INGOT',
                       'GOLD_INGOT',
                       'DIAMOND',
                       'INK_SACK:4',
                       'EMERALD',
                       'REDSTONE',
                       'QUARTZ',
                       'OBSIDIAN',
                       'GLOWSTONE_DUST',
                       'GRAVEL',
                       'ICE',
                       'NETHERRACK',
                       'SAND',
                       'ENDER_STONE']
        message = ''
        maxed = 0
        for collection in collections:
            if collection == 'COBBLESTONE':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          40000,
                          70000]
            elif collection == 'COAL' or collection == 'IRON_INGOT' or collection == 'GOLD_INGOT' or collection == 'DIAMOND' or collection == 'QUARTZ' or collection == 'GLOWSTONE_DUST' or collection == 'GRAVEL':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'INK_SACK:4':
                req_xp = [250,
                          500,
                          1000,
                          2000,
                          10000,
                          25000,
                          50000,
                          100000,
                          150000,
                          250000]
            elif collection == 'EMERALD':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          5000,
                          15000,
                          30000,
                          50000,
                          100000]
            elif collection == 'REDSTONE':
                req_xp = [100,
                          250,
                          750,
                          1500,
                          3000,
                          5000,
                          10000,
                          25000,
                          50000,
                          200000,
                          400000,
                          600000,
                          800000,
                          1000000,
                          1200000]
            elif collection == 'OBSIDIAN':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000,
                          100000]
            elif collection == 'ICE':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          5000,
                          10000,
                          50000,
                          100000,
                          250000]
            elif collection == 'NETHERRACK':
                req_xp = [50,
                          250,
                          500]
            elif collection == 'SAND':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2500,
                          5000]
            elif collection == 'ENDER_STONE':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          15000,
                          25000,
                          50000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = self.translateIDName(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        msg = f"{col}: Level {self.comma(lvl)} - MAX\n"
                        maxed += 1
                    else:
                        progress = f"{self.comma(int(round(amount, 0)))}/{self.comma(next_lvl)}"
                        msg = f"{col}: Level {self.comma(lvl)} - {progress} Items\n"
                else:
                    progress = f"0/{self.comma(req_xp[0])}"
                    msg = f"{col}: Level 0 - {progress} Items\n"
                message += msg
        return maxed, len(collections), message

    def combatCollection(self, data: dict):
        collections = ['ROTTEN_FLESH',
                       'BONE',
                       'STRING',
                       'SPIDER_EYE',
                       'SULPHUR',
                       'ENDER_PEARL',
                       'GHAST_TEAR',
                       'SLIME_BALL',
                       'BLAZE_ROD',
                       'MAGMA_CREAM']
        message = ''
        maxed = 0
        for collection in collections:
            if collection == 'ROTTEN_FLESH' or collection == 'SPIDER_EYE' or collection == 'SULPHUR' or collection == 'SLIME_BALL' or collection == 'BLAZE_ROD' or collection == 'MAGMA_CREAM':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'BONE':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000,
                          150000]
            elif collection == 'STRING':
                req_xp = [60,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'ENDER_PEARL':
                req_xp = [50,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          15000,
                          25000,
                          50000]
            elif collection == 'GHAST_TEAR':
                req_xp = [20,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = self.translateIDName(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        msg = f"{col}: Level {self.comma(lvl)} - MAX\n"
                        maxed += 1
                    else:
                        progress = f"{self.comma(int(round(amount, 0)))}/{self.comma(next_lvl)}"
                        msg = f"{col}: Level {self.comma(lvl)} - {progress} Items\n"
                else:
                    progress = f"0/{self.comma(req_xp[0])}"
                    msg = f"{col}: Level 0 - {progress} Items\n"
                message += msg
        return maxed, len(collections), message

    def foragingCollection(self, data: dict):
        collections = ['LOG',
                       'LOG:1',
                       'LOG:2',
                       'LOG_2:1',
                       'LOG_2',
                       'LOG:3']
        message = ''
        maxed = 0
        for collection in collections:
            if collection == 'LOG':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2000,
                          5000,
                          10000,
                          30000]
            elif collection == 'LOG:1':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2000,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'LOG:2':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1,000,
                          2,000,
                          5,000,
                          10,000,
                          25,000]
            elif collection == 'LOG_2:1':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500,
                          5000,
                          10000,
                          25000,
                          50000]
            elif collection == 'LOG_2':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2000,
                          5000,
                          10000,
                          25000]
            elif collection == 'LOG:3':
                req_xp = [50,
                          100,
                          250,
                          500,
                          1000,
                          2000,
                          5000,
                          10000,
                          25000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = self.translateIDName(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        msg = f"{col}: Level {self.comma(lvl)} - MAX\n"
                        maxed += 1
                    else:
                        progress = f"{self.comma(int(round(amount, 0)))}/{self.comma(next_lvl)}"
                        msg = f"{col}: Level {self.comma(lvl)} - {progress} Items\n"
                else:
                    progress = f"0/{self.comma(req_xp[0])}"
                    msg = f"{col}: Level 0 - {progress} Items\n"
                message += msg
        return maxed, len(collections), message

    def fishingCollection(self, data: dict):
        collections = ['RAW_FISH',
                       'RAW_FISH:1',
                       'RAW_FISH:2',
                       'RAW_FISH:3',
                       'PRISMARINE_SHARD',
                       'PRISMARINE_CRYSTALS',
                       'CLAY_BALL',
                       'WATER_LILY',
                       'INK_SACK',
                       'SPONGE']
        message = ''
        maxed = 0
        for collection in collections:
            if collection == 'RAW_FISH':
                req_xp = [20,
                          50,
                          100,
                          250,
                          500,
                          1000,
                          2500,
                          15000,
                          30000,  
                          45000,
                          60000]
            elif collection == 'RAW_FISH:1':
                req_xp = [20,
                          50,
                          100,
                          250,
                          500,
                          1000,
                          2500,
                          5000,
                          10000]
            elif collection == 'RAW_FISH:2':
                req_xp = [10,
                          25,
                          50,
                          100,
                          200,
                          400,
                          800]
            elif collection == 'RAW_FISH:3':
                req_xp = [20,
                          50,
                          100,
                          150,
                          400,
                          800,
                          2400,
                          4800,
                          9000]
            elif collection == 'PRISMARINE_SHARD':
                req_xp = [10,
                          25,
                          50,
                          100,
                          200]
            elif collection == 'PRISMARINE_CRYSTALS':
                req_xp = [10,
                          25,
                          50,
                          100,
                          200,
                          400,
                          800]
            elif collection == 'CLAY_BALL':
                req_xp = [50,
                          100,
                          250,
                          1000,
                          2500]
            elif collection == 'WATER_LILY':
                req_xp = [10,
                          50,
                          100,
                          200,
                          500,
                          1500,
                          3000,
                          6000,
                          10000]
            elif collection == 'INK_SACK':
                req_xp = [20,
                          40,
                          100,
                          200,
                          400,
                          800,
                          1500,
                          2500,
                          4000]
            elif collection == 'SPONGE':
                req_xp = [20,
                          40,
                          100,
                          200,
                          400,
                          800,
                          1500,
                          2500,
                          4000]
            else:
                req_xp = []
            if len(req_xp) != 0:
                col = self.translateIDName(collection)
                if collection in data['collection']:
                    next_lvl = 0
                    amount = data['collection'][collection]
                    lvl = 0
                    for level in req_xp:
                        if amount >= level:
                            lvl += 1
                            pass
                        elif amount < level:
                            next_lvl = level
                            break
                    if lvl >= len(req_xp):
                        msg = f"{col}: Level {self.comma(lvl)} - MAX\n"
                        maxed += 1
                    else:
                        progress = f"{self.comma(int(round(amount, 0)))}/{self.comma(next_lvl)}"
                        msg = f"{col}: Level {self.comma(lvl)} - {progress} Items\n"
                else:
                    progress = f"0/{self.comma(req_xp[0])}"
                    msg = f"{col}: Level 0 - {progress} Items\n"
                message += msg
        return maxed, len(collections), message

    def getAverage(self, lst: list) -> float:
        return sum(lst) / len(lst)

    def getMinionSlots(self, data: dict) -> int:
        slts = 5
        slots = 5
        req_unique=[5,
                    15,
                    30,
                    50,
                    75,
                    100,
                    125,
                    150,
                    175,
                    200,
                    225,
                    250,
                    275,
                    300,
                    350,
                    400,
                    450,
                    500,
                    550]
        minions = []
        for member in data['profile']['members']:
            member = data['profile']['members'][member]
            try:
                for minion in member['crafted_generators']:
                    if minion not in minions:
                        minions.append(minion)
            except:
                continue
        rexp = len(minions)
        for level in req_unique:
            if rexp >= level:
                slts += 1
            elif rexp < level:
                slots = slts
                break
        return slots

    def getCatacombsLevel(self, xp):
        req_xp=[50,
                75,
                110,
                160,
                230, 
                330,
                470,
                670,
                950,
                1340,
                1890,
                2665,
                3760,
                5260,
                7380,
                10300, 
                14400, 
                20000, 
                27600, 
                38000, 
                52500, 
                71500,
                97000, 
                132000,
                180000,
                243000, 
                328000, 
                445000,
                600000,
                800000,
                1065000,
                1410000,
                1900000,
                2500000,
                3300000,
                4300000,
                5600000,
                7200000,  
                9200000, 
                12000000, 
                15000000,  
                19000000, 
                24000000,
                30000000, 
                38000000,
                48000000, 
                60000000,
                75000000,
                93000000, 
                116250000]
        lvl = 0
        rexp = xp
        for level in req_xp:
            if rexp >= level:
                rexp -= level
                lvl += 1
                pass
            elif rexp < level:
                break
        return lvl

class hypixel:
    """ Class for interacting with Hypixel's API """
    def __init__(self):
        self.session = ClientSession()  # Define aiohttp session.

    async def player(self, uuid: str) -> dict:
        """ Get Hypixel player data. """
        async with self.session.get('https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid) as response:
            return await response.json()

    async def mcserver(self, ip: str, port: str=25565) -> dict:
        """ Get Hypixel player data. """
        async with self.session.get(f'https://api.mcsrvstat.us/2/{ip}:{port}') as response:
            return await response.json()

    async def counts(self) -> dict:
        """ Get Hypixel server counts. """
        async with self.session.get('https://api.hypixel.net/gameCounts?key=' + API_KEY) as response:
            return await response.json()

    async def leaderboards(self) -> dict:
        """ Get Hypixel leaderboards. """
        async with self.session.get('https://api.hypixel.net/leaderboards?key=' + API_KEY) as response:
            return await response.json()

    async def key(self) -> dict:
        """ Get info on your Hypixel API key. """
        async with self.session.get('https://api.hypixel.net/key?key=' + API_KEY) as response:
            return await response.json()

    async def watchdog(self) -> dict:
        """ Get Hypixel Watchdog stats. """
        async with self.session.get('https://api.hypixel.net/watchdogstats?key=' + API_KEY) as response:
            return await response.json()

    async def guild(self, name: str) -> dict:
        """ Find a guild by name and return guild data. """
        async with self.session.get('https://api.hypixel.net/findGuild?key=' + API_KEY + '&byName=' + name) as response:
            data = await response.json()
            gid = data['guild']
        if gid is None:
            raise ValueError
        async with ClientSession() as session:
            async with session.get('https://api.hypixel.net/guild?key=' + API_KEY + '&id=' + gid) as response:
                return await response.json()

    async def getname(self, uuid: str):
        """ Get a player's name using Mojang API. """
        async with self.session.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid) as response:
            data = await response.json()
        try:
            return data['name'].replace('_', '\_')
        except:
            return None

    async def playerguild(self, uuid) -> str:
        """ Get the name of the guild a player is in. """
        async with self.session.get('https://api.hypixel.net/guild?key=' + API_KEY + '&player=' + uuid) as response:
            data = await response.json()
            if data['guild'] is None:
                return 'None'
            return data['guild']['name']

    async def boosters(self, game: str = None):
        async with self.session.get('https://api.hypixel.net/boosters?key=' + API_KEY) as response:
            data = await response.json()
        if game is None:
            return len(data['boosters'])
        else:
            boosters = data['boosters']
            if len(boosters) == 0:
                raise ValueError
            return boosters

    async def status(self):
        async with self.session.get("https://status.hypixel.net/history.json") as response:
            return await response.json()

    class skyblock:
        """ Class for interacting with Hypixel's Skyblock API. """

        def __init__(self):
            self.session = ClientSession()

        async def profile(self, profile) -> dict:
            async with self.session.get(
                       'https://api.hypixel.net/skyblock/profile?key=' + API_KEY + '&profile=' + profile) as response:
                return await response.json()

        async def auctions(self, profile) -> dict:
            async with self.session.get(
                       'https://api.hypixel.net/skyblock/auction?key=' + API_KEY + '&profile=' + profile) as response:
                return await response.json()

        async def bazaar(self) -> dict:
            async with self.session.get(
                       'https://api.hypixel.net/skyblock/bazaar?key=' + API_KEY) as response:
                return await response.json()

        async def news(self, title):
            async with self.session.get(
                       'https://api.hypixel.net/skyblock/news?key=' + API_KEY) as response:
                data = await response.json()
            if title is None:
                return data['items']
            for item in data['items']:
                if item['title'].lower() == title.lower():
                       return item
            return None



utils = utils()
hypixel = hypixel()
hypixel.skyblock = hypixel.skyblock()
