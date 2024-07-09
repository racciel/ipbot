import requests
import asyncio
import time
import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

prviput = True
ipstari = requests.get('https://ipinfo.io/ip').text

@tasks.loop(minutes=1)
async def test():
    global ipstari
    channel = client.get_channel(865124359181172736)
    ip = requests.get('https://ipinfo.io/ip').text
    
    if ip != ipstari:
        await channel.send('IP servera je: ' + ip)
        ipstari = ip

    print(ip)

@client.event
async def on_ready():
    global prviput
    prviput = True
    test.start()

@client.event
async def on_resumed():
    print('reconnected')

@client.event
async def on_message(message):
    if message.content == '-ip?':
        response = requests.get('https://ipinfo.io/ip').text
        await message.channel.send('NA! ' + response)
    
client.run(TOKEN)
