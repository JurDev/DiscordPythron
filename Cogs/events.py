import discord
import random
import json
import asyncio
import os
import emoji
from discord.ext import commands
from discord.utils import get

class EventsCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_remove(self,ctx, member):
        print(f'{member} .')
        await ctx.send(f'{member}Doei!, Heeft de server verlaten.')

    @commands.Cog.listener()
    async def on_member_join(self,ctx, member):
        print(f'{member} .')
        await ctx.send(f'{member}Welkom, in Pythron.')


    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Dat Werkt NIET!')



def setup(bot):
    bot.add_cog(EventsCog(bot))
