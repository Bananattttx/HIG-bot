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

    await bot.process_commands(message)

bot.run(TOKEN)
