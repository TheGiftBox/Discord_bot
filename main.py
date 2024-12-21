import os
import discord
from discord.ext import commands
from myserver import server_on

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("ตื่นแย้วว!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1319650372347891712)
    text = f"{member.mention} join the server"

    await channel.send(text)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1319650372347891712)
    text = f"{member.mention} has left the server"

    await channel.send(text)


server_on

bot.run(token)