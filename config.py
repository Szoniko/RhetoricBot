import praw, hypixel

"""

CONFIGURATION FILE FOR THE RHETORIC BOT
Please follow the instructions next to variables 

"""

# discord bot token

auth = "PASTE_YOUR_TOKEN_HERE"

# reddit app 

reddit = praw.Reddit(
    client_id="client id",
    client_secret="client secret",
    user_agent="this can be anything",
    username="username",
    password="password"
)

# hypixel api key(s)
# You can use one, or multiple, but preferably one

hypixel.setKeys(['API_KEY_HERE'])

# The prefix of the bot

command_prefix = "."

# leave and join respones, they have to be arrays
# the {member.mention} represent the joining users name 

join_responses = [f"{member.mention} joined the guild"]

# leave 

leave_responses = [f"{member.mention} left the guild."]