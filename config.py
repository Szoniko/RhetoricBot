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