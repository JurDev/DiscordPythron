import discord
import json, random, requests, datetime, time, urllib.request, io, os, aiohttp

from typing import Union
from discord.ext import commands
from discord.utils import get
from random import randint

global mm

class misccommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['Discordpythron'])
    async def ping(self,ctx):
        resp = await ctx.send('De bal komt terug...')
        diff = resp.created_at - ctx.message.created_at
        await resp.edit(content=f'Pong! dat duurde {1000 * diff.total_seconds():.1f}miliseconde.')

    @commands.command(aliases=['8ball'])
    async def _Waarzegger(self, ctx, *, question):
        responses = [
                "Zeker weten.",
                "Ik Twijfel Maar Ja!.",
                "Zonder Twijfel.",
                "Ja Zeker Weten.",
                "Je kan Er Op Rekenen.",
                "Zoals Ik Het Zie JA!.",
                "Waarschijnlijk Wel.",
                "Goede Uitkomst.",
                "Ja.",
                "De Tekenen Zeggen Ja.",
                "Probeer opnieuw.",
                "Vraag het later opnieuw.",
                "Het is beter als ik je vraag nu niet beantwoord.",
                "kan ik nu niet beantwoorden.",
                "concentreer je en vraag het opnieuw.",
                "Reken er maar niet op.",
                "Nee.",
                "Mijn bronnen zeggen nee.",
                "Dat gaat niet goed aflopen.",
                "ik betwijfel je vraag."]
        await ctx.send(f': {question}: {random.choice(responses)}')



    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
        '''Display Info'''
        member = ctx.author if not member else member

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name="Name:", value=member.display_name)
        embed.add_field(name='Acount created at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
        embed.add_field(name="Joined the server:", value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
        embed.add_field(name=f'Roles({len(roles)}):', value=''.join([role.mention for role in roles]))

        await ctx.send(embed=embed)
    #Rekenmachine
    @commands.command()
    async def plus(self, ctx, a:int, b:int):
        await ctx.send(a+b)

    @commands.command()
    async def min(self, ctx, a:int, b:int):
        await ctx.send(a-b)

    @commands.command()
    async def keer(self, ctx, a:int, b:int):
        await ctx.send(a*b)

    @commands.command()
    async def deel(self, ctx, a:int, b:int):
        if b==0:
            ans="0"
        else:
            ans=a/b
        await ctx.send(ans)


def setup(bot):
    bot.add_cog(misccommands(bot))
