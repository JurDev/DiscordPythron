import asyncio
import random
from asyncio import queues
import discord
import youtube_dl
import json
import shutil
import os
from discord.ext import commands
from discord.utils import get
from pyowm import OWM
owm = OWM('446527f8a2b47070f927ab4c4f643ef8')
global mm

client = commands.Bot(command_prefix='!')
client.remove_command('help')
client.fetch_offline_members = True


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="!Help"))
    print('DiscordPythron staat aan')


extensions = ['Cogs.events', 'Cogs.misc commands', 'Cogs.Music', 'Cogs.Activity', 'Cogs.Help', 'Cogs.random',]

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

#functie Coinflip
@client.command()
async def coinflip(ctx):
    choices = ["Kop" , "Munt"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

#functie weathermap
@client.command()
async def weer(ctx):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Zuid-Holland, NL')
    w = observation.weather
    # Weather details
    wind = w.wind()  # {'speed': 4.6, 'deg': 330}
    temperature = w.temperature('celsius')  # {'temp_max': 10.5 'temp': 9.7 'temp_min': 9.0}
    # Search current weather observations in the surroundings of
    # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
    await ctx.send(f"In Zuid Holland\n" f"is het nu {temperature['temp']} graden\n" f"en de windsnelheid is {wind['speed']} m/s\n")

#functie Info
@client.command()
async def info(ctx):
    embed = discord.Embed(
        title = 'Informatie',
        description = 'Deze bot is gemaakt door: Jurwin, Thomas, Scotty, Yannick',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text='Dank u wel voor het gebruik van onze bot!')
    embed.set_image(url='https://cdn.discordapp.com/attachments/722524544472055819/726788868002545725/output-onlinepngtools12.png')
    embed.set_author(name='Informatie over onze Discordbot!')
    embed.add_field(name='Waarom deze bot?', value='Wij hebben deze bot gemaakt als doel voor ons project. Het leek ons leuk om een bot te gaan maken omdat wij veel bezig zijn in de omgeving discord en er dus veel gebruik van maken. Wij zijn nu afhankelijk van andere bots van buitenaf en met onze bot weten we wat deze bot allemaal kan doen. Dit vinden wij interessant en natuurlijk ook heel leuk om te weten hoe dit nou werkt!', inline=False)
    embed.add_field(name='Commando', value='!Play, !Leave, !coinflip, !join, !ping, !help, !tag', inline=True)

    await ctx.send(embed=embed)



client.run('Njg0MzYzMjgyNTg0MTc0NTky.XrsGAA.nEZdAEAW2SHwEzCx1Ur8wWfwtRI')
