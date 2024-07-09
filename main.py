import requests
import asyncio
import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

ipstari = requests.get('https://ipinfo.io/ip').text

@tasks.loop(minutes=1)
async def check_ip():
    global ipstari
    channel = client.get_channel(865124359181172736)
    ip = requests.get('https://ipinfo.io/ip').text
    
    if ip != ipstari:
        await channel.send('IP servera je: ' + ip)
        ipstari = ip

    print(ip)

@client.event
async def on_ready():
    channel = client.get_channel(865124359181172736)
    ip = requests.get('https://ipinfo.io/ip').text
    await channel.send('Pokrećem se! Trenutna IP adresa servera je: ' + ip)
    check_ip.start()

@client.event
async def on_resumed():
    print('reconnected')

@client.event
async def on_message(message):
    if message.content == '-ip?':
        response = requests.get('https://ipinfo.io/ip').text
        await message.channel.send('NA! ' + response)
    
client.run(TOKEN)

