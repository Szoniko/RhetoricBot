import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
import praw

auth = "you aint getting it"

reddit = praw.Reddit(
    client_id="client id",
    client_secret="client secret",
    user_agent="this can be anything",
    username="username",
    password="password"
)

client: Bot = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("ready")

##################################################

@client.command()
async def ping(ctx):
    ctx.send("pong")
    
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
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

@client.command()
async def sub(ctx,subred):
    subreddit = reddit.subreddit(subred)
    all_subs = []

    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)

    em.set_image(url = url)


client.run(auth)
