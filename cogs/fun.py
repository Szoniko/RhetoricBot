import discord
import config
import requests
import random
from discord.ext import commands


class Fun(commands.Cog):

    # initialize
    def __init__(self, client):
        self.client = client


    # confirm that cog loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 'fun' loaded")

    """USE THE DECORATOR @commands.command INSTEAD OF @client.command"""

    @commands.command(aliases=["_.", "-.", ".."])
    async def imannoyed(self, ctx):
        await ctx.send("why are you annoyed?")

    @commands.command()
    async def hentai(self, ctx):
        await ctx.send("`https://bit.ly/2KAOWap`")

    @commands.command(aliases=["cmafomt", "imnotafurry"])
    async def callmeafurryonemoretime(self, ctx):
        embed = discord.Embed(
            title="I swear",
            description="If you say it one more goddamn time",
            colour=discord.Colour.magenta()
        )
        embed.add_field(name="Im gonna break your fucking head",
                        value="AAAAAAAAAAAAAAAH")
        await ctx.send(embed=embed)

    @commands.command()
    async def duck(self, ctx):
        url = requests.get("https://random-d.uk/api/v2/random").json()['url']
        await ctx.send(url)

    @commands.command()
    async def chickennungget(self, ctx):

        def probably(chance):
            return random.random() < chance

        #80% chance
        common_responses = [
             "chicken nuggets were created by a scientist?",
             "chicken nuggets were used to solve a food storage problem?",
             "the largest chicken nugget ever made weighed 23.17kg? (51.1 lbs)",
             "chicken nuggets are one of the prime reasons for obesity and health problems in children?",
             "the chicken nugget was invented by Robert C. Baker, a professor at Cornell University?"
        ]

        #15% chance
        rare_responses = [
            "a chicken nugget will befriend you someday?",
            "a chicken nugget might become your new best friend?",
            "you should give me chicken nuggets :)",
            "a chicken nugget will be saved each time you use this command?"
        ]

        #4% chance
        legendary_responses = [
            "a chicken nugget is behind you?",
            "there's a chance you will choke on chicken nuggets?",
            "McDonalds sells chicken nuggets?",

        ]

        #1% chance
        supreme_responses = [
            "Please let me out of your basement, i'm sick and tired of writing all these stupid c̵͙̈́̑͊ḣ̵̢̺͎̫̜̩̙̮̣̄̎͌̒́̊̾͝i̵̧̹͉͓̮̳͇̻̜͒̌̀͌͑̉̒̈́̓̆̂͛͆͜͝ͅͅc̶̡̥̠͔̘̽͊̀̆̍͗͒̇̂̃͘͠͠͠ḱ̶͚̩̹͝ḙ̶̓̍͌̾̎̓̐̌͊̚͠n̵̢̨̨̡̟͍͇̠̳͓̘̤̣̓́̿̏͐̋͛̋̈͂͌͛͠͠͝ ̵̼͍͙̳͚̩̙̫͍̜̂̕n̸͇͚̹͓̏͑̎̒u̴̜̩͇̥̿͐͘g̸̳̫̝̈́ͅ---- did you know that McDonalds sells chicken nuggets?̸̥̣̟̙͍̞̖̣",
            "c̵͙̈́̑͊ḣ̵̢̺͎̫̜̩̙̮̣̄̎͌̒́̊̾͝i̵̧̹͉͓̮̳͇̻̜͒̌̀͌͑̉̒̈́̓̆̂͛͆͜͝ͅͅc̶̡̥̠͔̘̽͊̀̆̍͗͒̇̂̃͘͠͠͠ḱ̶͚̩̹͝ḙ̶̓̍͌̾̎̓̐̌͊̚͠n̵̢̨̨̡̟͍͇̠̳͓̘̤̣̓́̿̏͐̋͛̋̈͂͌͛͠͠͝ ̵̼͍͙̳͚̩̙̫͍̜̂̕n̸͇͚̹͓̏͑̎̒u̴̜̩͇̥̿͐͘g̸̳̫̝̈́ͅg̸̻̱̪͎̜͈͖̗͍̱͈̯̩͓̃̈́́̈̈́͌͛̕̕̕ͅe̸̛̥̣̟̙͍̞̖̣̽̅̂̈̿͘̕ṱ̴̛̜̂͌̽͑͌̓͑̇͆̄̿̂͘͠"
        ]

        if (probably(1 / 100)):
            choice = random.choice(supreme_responses)
            await ctx.send(choice)

        elif (probably(4 / 100)):
            choice = random.choice(legendary_responses)
            await ctx.send("Did you know that " +choice)

        elif (probably(15 / 100)):
            choice = random.choice(rare_responses)
            await ctx.send("Did you know that " +choice)

        elif (probably(80 / 100)):
            choice = random.choice(common_responses)
            await ctx.send("Did you know that " +choice)

        else:
            choice = random.choice(common_responses)
            await ctx.send("Did you know that " +choice)

# don't touch this
def setup(client):
    client.add_cog(Fun(client))
