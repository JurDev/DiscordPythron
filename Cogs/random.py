import discord
from discord.ext import commands

import io, random, json

from typing import Optional


class RNGCog(commands.Cog, name='Rng'):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name='randnum', aliases=['randnumber'])
    async def random_num(self, ctx, min: int = 0, max: int = 10):
        if max <= min:
            max, min = min, max
        await ctx.send(random.randint(min, max))

    @commands.command(name='rol')
    async def Dobbelsteen(self, ctx, num_rolls: Optional[int] = 1, faces: Optional[int] = 6, sorted: bool = False):
        if not (1 <= num_rolls <= 999):
            return await ctx.send('De dobbelsteen moet tussen 1 en 999 keer gerold worden')
        if not (1 <= faces <= 999):
            return await ctx.send('De dobbelsteen moet tussen 1 en 999 kanten hebben')
        rolls = []
        for _ in range(num_rolls):
            rolls.append(random.randint(1, faces))
        sort = ''
        multi = ''
        if sorted:
            rolls.sort()
            sort = 'Sorted '  # Empty string if unsorted
        if num_rolls != 1:
            multi = 's'
        separator = ' '  # Space between each element in list when outputting

        embed = discord.Embed(colour=discord.Color.dark_teal(),
                              description=f'{sort}Resultaat voor het rollen van de dobbelsteen met {faces} kanten {num_rolls} keer{multi}:')
        embed.add_field(name='Rollen', value=separator.join(str(roll) for roll in rolls))
        embed.add_field(name='Totaal', value=sum(rolls), inline=False)
        try:
            await ctx.send(embed=embed)
        except discord.errors.HTTPException:
            await ctx.send('Discord kan deze hoeveelheid getallen niet aan.\n'
                           'Probeer het opnieuw met een kleinere aantal')

    @commands.command(name='Keuze')
    async def random_choice(self, ctx, *choices: commands.clean_content):
        if len(choices) < 2:
            return await ctx.send('Ik heb meer keuzes nodig :sob:')

        await ctx.send(random.choice(choices))






def setup(bot):
    bot.add_cog(RNGCog(bot))
