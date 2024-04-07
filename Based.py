import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def toplama(ctx, s1=0, s2=5):
    await ctx.send(s1+s2)

@bot.command()
async def cıkarma(ctx, s1=0, s2=5):
    await ctx.send(s1-s2)

@bot.command()
async def carpma(ctx, s1=0, s2=5):
    await ctx.send(s1*s2)

@bot.command()
async def bolme(ctx, s1=0, s2=5):
    await ctx.send(s1/s2)

@bot.command()
async def oyun1(ctx, s1=0):
    x=random.randint(1,6)
    if x == s1:
        await ctx.send("doğru bildin")
    else:
        await ctx.send(f"tutturamadın" ,{x}, "gelmişti.",s1)

@bot.command()
async def oyun2(ctx, s1):
    x=random.randint(1,3)
    if x == 1:
        x="yazı"

    if x == 2:
        x="tura"

    if x == 3:
        x="dik"

    s1= s1.lower()
    if s1==x:
        await ctx.send("doğru bildin!")
    else:
        await ctx.send(f"yanlış bildin cevap: {x}")

bot.run("TOKEN")
