import praw
import random
from discord_webhook import DiscordWebhook

modelh = ["h", "ℋ", "*h*", "**h**", "~~literally anything else~~ h", "h is awesome :]", "h :]", "# h", "# **h**"]
ver_rare_responses = "H is gud, 8ch is gud, u/pedrogabriellima13 is not, G is chill, u/ethangaming7640 is ver h, u/actual_tumbleweed814 is ver h"
rare_responses = ["H is gud, u/ethangaming7640 is ver H", "H is gud, u/actual_tumbleweed817 is ver h"]
main_responses = ["H is gud", "8ch is gud", "H is gud, u/PedroGabrielLima13 is not", "# Is H gud? \n Yes", "# H \n # is \n # gud."]

reddit = praw.Reddit(
    client_id="###",
    client_secret="###",
    user_agent="HIG-bot by u/blahajttttx",
    username="HIG-bot",
    password="###"
)
webhook_url = "https://discord.com/api/webhooks/###"
user_ping = "<@###>"

H = reddit.subreddit("TheLetterH")


for comment in H.stream.comments(skip_existing=True):
    # reply to u/h-bot-model-h in r/theletterh
    if comment.author and comment.author.name == "h-bot-model-h" and comment.body in modelh:
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
        webhook = DiscordWebhook(url=webhook_url, content=f"{user_ping} \n new comment: <{post_url}>")
        response = webhook.execute()
    
    # reply to u/i-bot9000 saying "**"H is gud"** - u/hig-bot" in r/theletterh
    if comment.author and comment.author.name == "i-bot9000" and comment.body == '**"H is gud"** - u/HIG-bot':
        comment.reply('"HIU" - u/i-bot9000')

        post_url = f"https://www.reddit.com{comment.submission.permalink}"
        print(f"new quote comment: {post_url}")

        # post logs in discord channel
        webhook = DiscordWebhook(url=webhook_url, content=f"{user_ping} \n new quote comment: <{post_url}>")
        response = webhook.execute()