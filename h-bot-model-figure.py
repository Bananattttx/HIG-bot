import praw
import time
import random
import assets

reddit = assets.model_figure

subreddit = reddit.subreddit('TheLetterH')
neeeerrrdd = ["hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
              "e (tHere is a one in like a bajillion cHance that i reply witH e. if you see tHis, consider it qood luck)",
              "H", "pc", "h is cool", "[}{]", "h"]
modelh = ["h", "ℋ", "*h*", "**h**", "~~literally anything else~~ h", "h is awesome :]", "h :]", "# h", "# **h**"]

for comment in subreddit.stream.comments(skip_existing=True):
    if comment.author and comment.author.name == 'h-bot10000' and comment.body in neeeerrrdd:
        time.sleep(120)
        comment.refresh()

        replied = any(reply.author and reply.author.name == 'h-bot-model-h' and reply.body in modelh for reply in comment.replies)
        if not replied:
            comment.reply(random.choice(modelh))
            
            post_url = f"https://www.reddit.com{comment.submission.permalink}"
            print(f"new comment: {post_url}")