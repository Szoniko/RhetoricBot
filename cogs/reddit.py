import discord, random, config, praw
from discord.ext import commands


class Reddit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is online')   

    @commands.command()
    async def meme(self, ctx):
        subreddit = config.reddit.subreddit("memes")
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title = name)

        em.set_image(url = url)
        
        await ctx.send(embed= em)

    @commands.command()
    async def sub(self, ctx,subred):
        subreddit = config.reddit.subreddit(subred)
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title = name)

        em.set_image(url = url)

def setup(client):
    client.add_cog(Reddit(client))