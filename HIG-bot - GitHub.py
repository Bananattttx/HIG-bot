import praw

reddit = praw.Reddit(
    client_id="###",
    client_secret="###",
    user_agent="HIG-bot by u/BananattttxNew",
    username="###",
    password="###"
)

subreddit = reddit.subreddit("TheLetterH")

for comment in subreddit.stream.comments(skip_existing=True):
    if comment.author and comment.author.name == "h-bot-model-h" and comment.body == "h":
        comment.reply("H is gud")
