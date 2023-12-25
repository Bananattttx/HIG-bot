import praw

modelh = ["h", "ℋ", "*h*", "**h**", "~~literally anything else~~ h", "h is awesome :]", "h :]", "# h", "# **h**"]

reddit = praw.Reddit(
    client_id="###",
    client_secret="###",
    user_agent="HIG-bot by u/BananattttxNew",
    username="HIG-bot",
    password="###"
)

subreddit = reddit.subreddit("TheLetterH")

for comment in subreddit.stream.comments(skip_existing=True):
    if comment.author and comment.author.name == "h-bot-model-h" and comment.body in modelh:
        comment.reply("H is gud")
        print("new comment")
