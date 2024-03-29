import praw
import random
import assets
from discord_webhook import DiscordWebhook

print("HIG-bot is running")

modelh = ["h", "ℋ", "*h*", "**h**", "~~literally anything else~~ h", "h is awesome :]", "h :]", "# h", "# **h**"]
ver_rare_responses = "H is gud, 8ch is gud, u/pedrogabriellima13 is not, G is chill, u/ethangaming7640 is ver h, u/actual_tumbleweed814 is ver h, u/ismashkeyboards69 is ver h"
rare_responses = ["H is gud, u/ethangaming7640 is ver H", "H is gud, u/actual_tumbleweed814 is ver h", "H is gud, u/ismashkeyboards69 is ver h"]
main_responses = ["H is gud", "8ch is gud", "H is gud, u/PedroGabrielLima13 is not", "# Is H gud? \n Yes", "# H \n # is \n # gud."]

reddit = assets.HIG_bot

H = reddit.subreddit("TheLetterH")
reply_to = ["h-bot-model-h", "h-bot-model-figure"]

for comment in H.stream.comments(skip_existing=True):
    # reply to u/h-bot-model-h in r/theletterh
    if comment.author and comment.author.name in reply_to and comment.body in modelh:
        if random.randint(1, 100) == 1:
            # 1 in 100 chance
            comment.reply(ver_rare_responses)
        elif random.randint(1, 10) == 1:
            # 1 in 10 chance
            comment.reply(random.choice (rare_responses))
        else: 
            comment.reply(random.choice (main_responses))
        
        post_url = f"https://www.reddit.com{comment.submission.permalink}"
        print(f"new comment: {post_url}")

        # post logs in discord channel
        webhook_text = f"{assets.HIG_ping} \n # new post in r/theletterh \n **{comment.body}**  |  u/{comment.author} \n <{post_url}>"
        webhook = DiscordWebhook(url=assets.HIG_webhook, content=webhook_text)
        response = webhook.execute()
    
    # reply to u/i-bot9000 saying "**"H is gud"** - u/hig-bot" in r/theletterh
    if comment.author and comment.author.name == "i-bot9000" and comment.body == '**"H is gud"** - u/HIG-bot':
        comment.reply('"HIU" - u/i-bot9000')

        post_url = f"https://www.reddit.com{comment.submission.permalink}"
        print(f"new quote comment: {post_url}")

        # post logs in discord channel
        webhook = DiscordWebhook(url=assets.HIG_webhook, content=f"new quote comment: <{assets.HIG_ping}>")
        response = webhook.execute()