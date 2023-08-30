import discord
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

    if message.content.lower() == 'h':
        await message.channel.send('H is gud')

    await bot.process_commands(message)

bot.run(TOKEN)
