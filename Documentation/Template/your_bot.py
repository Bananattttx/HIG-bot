import praw

reddit = praw.Reddit(
    client_id="CLIENT ID",
    client_secret="CLIENT SECRET",
    user_agent="BOT NAME by MAIN ACC",
    username="BOT USERNAME",
    password="BOT PASSWORD"
)

subreddit = reddit.subreddit("LETTER SUBREDDIT")

for comment in subreddit.stream.comments(skip_existing=True):
    if comment.author and comment.author.name == "BOT TO REPLY TO" and comment.body == "BOT REPLY TEXT TO REPLY TO":
        comment.reply("BOT REPLY")
        print("new comment")
