import discord
import random
import assets
from discord.ext import commands
from typing import Optional

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!hig ', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# !hig h
@bot.command()
async def h(ctx):
    await ctx.send("H is gud")

# !hig echo [text]
@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)

# !hig ig [text] [argument(optional)]
@bot.command()
async def ig(ctx, arg1, arg2: Optional[str] = "gud"):
        strings = {"gud" : "__arg1__ is gud",
                   "chill" : "H is gud, __arg1__ is chill",
                   "verh" : "H is gud, __arg1__ is ver H",
                   "not" : "H is gud, __arg1__ is not"
                   }
        if arg2 in strings:
                await ctx.send(strings[arg2].replace("__arg1__", arg1))
        else:
                await ctx.send(f"the argument '{arg2}' was not found")

# !hig himg [image name]
strings = {"dancing" : "https://tenor.com/view/letter-h-gif-9063752",
           "fire" : "https://media.istockphoto.com/id/178615036/photo/flamy-symbol.jpg?s=612x612&w=0&k=20&c=-hYe_dtt_DWyWUxEu8TiEIzYDjzvZQEf7lHq2Q_7aMc="
           }
@bot.command()
async def himg(ctx, arg):
        if arg in strings:
                await ctx.send(strings[arg])
        else:
                await ctx.send(f"the image '{arg}' was not found")

# !hig chain [chain text]
@bot.command()
async def chain(ctx, *, arg):
    strings = ["google en passant", "holy hell", "new response just dropped", "actual zombie", "call the exorcist", "bishop goes on vacation, never comes back",
           "knightmare fuel", "pawn storm incoming", "checkmate or riot", "queen sacrifice, anyone", "rook in the corner, plotting world domination",
           "ignite the chessboard", "*end of chain*"]
    if arg in strings:
          await ctx.send(strings[int(strings.index(arg)) + 1])
    else:
         await ctx.send("chain reply not found")

# !hig reply [command]
@bot.command()
async def reply(ctx, *, arg):
    H_varients = ["8ch", "aitch", "HHH", "𐒎", "🇭"]
    if arg == 'h' or arg in H_varients:
        if random.randint == 1:
            reply = f"{random.choice(H_varients)} is gud"
        else:
            reply = "H is gud"
    if arg == 'heijak':
        varients = ["heijak is gud", "h🤝e🤝i🤝j🤝a🤝k"]
        reply = random.choice(varients)
    if arg == 'h is gud':
        reply = "that's my line :("
    if arg == 'our h is gud':
        reply = "that's our line"
    if arg in ['h is mid', 'h is mediocre', 'h is bad', 'h sucks', 'fuck h']:
        varients = ["no it's not", "***NOPE***"]
        reply = random.choice(varients)
    if arg == 'awesome':
        reply = 'hawesome'
    if arg == 'h is h':
        reply = "https://cdn.discordapp.com/attachments/1145410835582287945/1146444794571264092/image.png"
    if arg == 'gh':
        varients = ["g🤝h", "H is gud, G is chill"]
        reply = random.choice(varients)
    if arg == 'our h':
        if random.randint(1,5) == 1:
            reply = "credts to: @jiffy6770 https://cdn.discordapp.com/attachments/1145410835582287945/1146725428879425656/Screenshot_20230831_111425_Sketchbook.jpg"
        else:
            reply = "our H is gud"
    if arg == 'blahaj':
        reply = 'blåhaj is gud'
    if arg == 'gaych':
        reply = 'gaych is gud, gaych is life'
    if arg == '🪑':
        reply = '🪑 is 🪑 :) 🪑'
    await ctx.send(reply)

bot.run(assets.HIG_test_token)