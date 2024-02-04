import discord
import random
import assets
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!HIG', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="the game of H"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if content == f'{bot.user.mention} h':
        if random.randint(1, 100) < 11:
            if random.randint(1, 5) == 1:
                await message.channel.send('8ch is gud')
            elif random.randint(1, 4) == 1:
                await message.channel.send('aitch is gud')
            elif random.randint(1,3) == 1:
                await message.channel.send('HHH is gud')
            elif random.randint(1,2) == 1:
                await message.channel.send('𐒎 is gud')
            else:
                await message.channel.send('🇭 is gud')
        else:
            await message.channel.send('H is gud')

    if content == f'{bot.user.mention} heijak':
        if random.randint(1, 2) == 1:
            await message.channel.send('heijak is gud')
        else:
            await message.channel.send('h🤝e🤝i🤝j🤝a🤝k')
    
    if content in [f'{bot.user.mention} h is gud', f'{bot.user.mention} H is gud', f'{bot.user.mention} 8ch is gud', f'{bot.user.mention} aitch is gud']:
        await message.channel.send("that's my line :(")

    if content == f'{bot.user.mention} our h is gud':
        await message.channel.send("that's our line")
    
    if content in [f'{bot.user.mention} h is mid', f'{bot.user.mention} h is mediocre', f'{bot.user.mention} h is bad', f'{bot.user.mention} h sucks', f'{bot.user.mention} fuck h']:
        if random.randint(1, 2) == 1:
            if content in [f'{bot.user.mention} h sucks']:
                await message.channel.send("no it dosen't")
            else:
                await message.channel.send("no it's not")
        else:
            await message.channel.send("𝙉𝙊𝙋𝙀")

    if content == f'{bot.user.mention} awesome':
        await message.channel.send('hawesome')
    
    if content == f'{bot.user.mention} h is h':
        await message.channel.send("https://cdn.discordapp.com/attachments/1145410835582287945/1146444794571264092/image.png")
    
    if content == f'{bot.user.mention} gh':
        if random.randint(1,2) == 1:
            await message.channel.send("g🤝h")
        else:
            await message.channel.send("H is gud, G is chill")

    if content == f'{bot.user.mention} our h':
        if random.randint(1,5) == 1:
            await message.channel.send("credts to: @jiffy6770 https://cdn.discordapp.com/attachments/1145410835582287945/1146725428879425656/Screenshot_20230831_111425_Sketchbook.jpg")
        else:
            await message.channel.send("our H is gud")
    
    if content == f'{bot.user.mention} blahaj':
         if random.randint(1, 100) < 11:
            if random.randint(1, 5) == 1:
                await message.channel.send('blåhaj is H')
            elif random.randint(1, 4) == 1:
                await message.channel.send('blåhaj is 8ch')
            elif random.randint(1,3) == 1:
                await message.channel.send('blåhaj blåhaj blåhaj is gud')
            elif random.randint(1,2) == 1:
                await message.channel.send('𝒷𝓁𝒶𝒽𝒶𝒿 is gud')
            else:
                await message.channel.send('<:blahaj:1148281434965016637> is gud')
         else:
             await message.channel.send('blåhaj is gud')

    if content == f'{bot.user.mention} gaych':
        if random.randint(1,10) == 1:
            await message.channel.send('🏳️‍🌈ch is gud, 🏳️‍🌈ch is life')
        else:
            await message.channel.send('gaych is gud, gaych is life')

    if content == f'{bot.user.mention} 🪑':
        await message.channel.send('🪑 is 🪑 :) 🪑')
    
    if content == f'{bot.user.mention} is H gud?':
        await message.channel.send("""YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES
                                   YES""")

    await bot.process_commands(message)

bot.run(assets.HIG_token)