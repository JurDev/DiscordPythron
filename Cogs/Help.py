import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="Discord Bot", description="Commando", color=0xeee657)
        embed.add_field(name="ping" , value="check je connectie", )
        embed.add_field(name="Waarzegger" , value="Beantwoord je vraag", )
        embed.add_field(name="Keuze" , value="Keuzes maken", )
        embed.add_field(name="rol" , value="Dobbelsteen", )
        embed.add_field(name="randnum" , value="Nummer tussen 0 en 10", )
        embed.add_field(name="say" , value="Bot phraise", )
        embed.add_field(name="user" , value="profiel informatie", )
        embed.add_field(name="Plus" , value="+", )
        embed.add_field(name="Min" , value="-", )
        embed.add_field(name="Keer" , value="*", )
        embed.add_field(name="Deel" , value="/", )
        embed.add_field(name="memo" , value="Later herinneren", )
        embed.add_field(name="remind" , value="Nu herinneren", )
        embed.add_field(name="level" , value="level checker", )
        embed.add_field(name="clear" , value="Chat clearen", )
        embed.add_field(name="join" , value="in de voice channel stappen", )
        embed.add_field(name="leave" , value="Verlaten", )
        embed.add_field(name="play" , value="Nummer spelen", )
        embed.add_field(name="pause" , value="Nummer Pauzeren", )
        embed.add_field(name="resume" , value="Nummer voortzetten", )
        embed.add_field(name="skip" , value="Nummer skippen", )
        embed.add_field(name="queue" , value="Nummer in de Queue zetten", )
        embed.add_field(name="weer", value="Weer in zuid-holland", )
        embed.add_field(name="coinflip", value="Coinflip", )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
