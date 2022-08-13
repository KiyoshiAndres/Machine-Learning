import os
import random

import io
import aiohttp


import discord

from discord.ext import commands
from dotenv import load_dotenv
from facebook_scraper import get_posts

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='hug', help='Hugs you')
async def pochita_hug(ctx):
    pochita_hugs = [
        "⊂(◉ω◉)つ",
        "⊂(◉ω◉⊂)",
        "⊂◉ω◉つ"
    ]

    response = random.choice(pochita_hugs)
    await ctx.send(response)

@bot.command(name='gm', help='Says good morning')
async def pochita_gm(ctx):
    response = "Woof! (Good morning)"
    await ctx.send(response)
    
seen_memes = []
    
@bot.command(name='meme', help='Sends you a meme')
async def image(ctx):
    meme_type = random.randint(1,10)
    page_id = ""
    if meme_type in [1,2,3]:
        #sess
        page_id = "100071414059478"
    elif meme_type in [4,10,9]:
        #moroha
        page_id = "100063615824623"
    elif meme_type == 5:
        #lewd
        page_id = "1762494480716410"
    elif meme_type == [6,7]:
        #good
        page_id = "582360348888586"
    elif meme_type == 8:
        #salmon
        page_id = "100043842653561"
        
    for post in get_posts(page_id, pages=5, cookies="/Users/kiyoshitakeuchi/Downloads/facebook.com_cookies.txt"):
        if post["images"] != []:
            if post["images"][0] in seen_memes:
                print("Seen this meme!")
                continue
                
            image_url = post["images"][0]
            seen_memes.append(post["images"][0])
            break
    await ctx.send(image_url)



@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Woof! (Hi {member.name}, good to have you here!)'
    )

    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "Pochita" in message.content:
        response = "Woof!"
        await message.channel.send(response)
        
    await bot.process_commands(message)

        
bot.run(TOKEN)