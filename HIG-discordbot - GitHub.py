import discord
import random
from discord.ext import commands

TOKEN = '###'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="H is gud"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if content in ['h', 'H', '8ch']:
        if random.randint(1, 100) == 1:
            await message.channel.send('8ch is gud')
        else:
            await message.channel.send('H is gud')
    
    if content in ['h is gud', 'H is gud', '8ch is gud']:
        await message.channel.send("that's my line :(")

    if content in ['h is mid', 'h is mediocre', 'h is bad', 'h sucks']:
        if random.randint(1, 2) == 1:
            if content in ['h sucks']:
                await message.channel.send("no it dosen't")
            else:
                await message.channel.send("no it's not")
        else:
            await message.channel.send("𝙉𝙊𝙋𝙀")

    if content == 'awesome':
        await message.channel.send('hawesome')
    
    if content == 'h is h':
        await message.channel.send("https://cdn.discordapp.com/attachments/1145410835582287945/1146444794571264092/image.png")

    await bot.process_commands(message)

bot.run(TOKEN)
