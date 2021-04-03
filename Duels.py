import discord
from discord.ext import commands
import newfile
import class_descriptions
import Duel_classes
import random
import sqlite3
import asyncio

class Duels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def duel(self, ctx, user: discord.Member):
        deterchar = 'N'
        if ctx.message.channel.id in list(self.bot.games.keys()):
            await ctx.send("Only one duel per channel is allowed.")
        else:
            if not self.bot.games:
                if user.id == ctx.author.id:
                    await ctx.send("You killed yourself in duel. Wait...you can't, duel somebody else.")
                elif user.bot:
                    await ctx.send("You can't duel bots, they can kill you with their botrickery!!")
                else:
                    deterchar = 'Y'
            else:
                for key in self.bot.games:
                    if user.id in self.bot.games[key]:
                        await ctx.send("Duel failed: Opponent is already in an ongoing duel!")
                    elif ctx.author.id in self.bot.games[key]:
                        await ctx.send("You can't go into a second duel with an ongoing duel.")
                    else:
                        deterchar = 'Y'
            if deterchar =='Y':
                await ctx.send(f"{user.name}, you have been challenged by {ctx.author.mention} for a duel. Do you accept? Type 'Y' to Accept and 'N' to reject.")

                def check(m):
                    return m.author.id == user.id and m.channel.id == ctx.channel.id and m.content in ['Y', 'y', 'n', 'N']

                try:
                    response = await self.bot.wait_for('message', check=check, timeout= 30.0)
                except asyncio.TimeoutError:
                    await ctx.send("Timeout exceeded, duel cannot be started.")
                    return

                else:
                    if response.content in ['y', 'Y']:
                        self.bot.games[ctx.message.channel.id] = [ctx.author.id, user.id]
                        await ctx.send("Duel has started. May the best warrior win!")

                        c = self.bot.conn.cursor()
                        c.execute('SELECT category, level, money, experience, defence, attack, magic, mainItem FROM UserCredentials WHERE name = (?)', (ctx.author.name,))
                        data = c.fetchall()
                        defenceP1 = int(data[0][4])
                        attackP1 = int(data[0][5])
                        magicP1 = int(data[0][6])
                        mainItemP1 = data[0][7]


                        c.execute('SELECT category, level, money, experience, defence, attack, magic, mainItem FROM UserCredentials WHERE name = (?)', (user.name,))
                        data2 = c.fetchall()
                        defenceP2 = int(data2[0][4])
                        attackP2 = int(data2[0][5])
                        magicP2 = int(data2[0][6])
                        mainItemP2 = data2[0][7]

                        MBoostP1 = 0

                        MBoostP2 = 0

                        for key in class_descriptions.Craftables[mainItemP1]:
                            if "Magic Boost" == key:
                                MBoostP1 = class_descriptions.Craftables[mainItemP1]["Magic Boost"][1]

                        ABoostP1 = class_descriptions.Craftables[mainItemP1]["Attack Boost"][1]

                        for key in class_descriptions.Craftables[mainItemP2]:
                            if "Magic Boost" == key:
                                MBoostP2 = class_descriptions.Craftables[mainItemP2]["Magic Boost"][1]
                            

                        ABoostP2 = class_descriptions.Craftables[mainItemP2]["Attack Boost"][1]

                        Player1 = Duel_classes.Player(attackP1 * (1 + ABoostP1), defenceP1, magicP1 * (1 + MBoostP1), 0, .80, .1)
                        Player2 = Duel_classes.Player(attackP2 * (1 + ABoostP2), defenceP2, magicP2 * (1 + MBoostP2), 0, .80, .1)

                        embedDuelLoad = discord.Embed(title= "Loading Duel", Description= f"**Tip:** {random.choice(class_descriptions.Duel_tips)}")
                        embedDuelLoad.add_field(name= "Player 1 Name", value = ctx.author.name)
                        embedDuelLoad.add_field(name= "Attack", value= Player1.attack)
                        embedDuelLoad.add_field(name="Defence", value=Player1.defence)
                        embedDuelLoad.add_field(name="Magic", value=Player1.magic)

                        embedDuelLoad.add_field(name= "Player 2 Name", value = user.name)
                        embedDuelLoad.add_field(name= "Attack", value= Player2.attack)
                        embedDuelLoad.add_field(name="Defence", value=Player2.defence)
                        embedDuelLoad.add_field(name="Magic", value=Player2.magic)

                        await ctx.send(embed= embedDuelLoad)


                    else:
                        await ctx.send("Request denied! Duel cancelled.")

    @commands.command()
    async def duelCogTest(self, ctx):
        await ctx.send("Working, yep, Cog's fine.")

    @commands.command()
    async def surrender(self, ctx):
        if self.bot.games:
            deterchar = 'N'
            for key in self.bot.games:
                if ctx.author.id in self.bot.games[key]:
                    deterchar = 'Y'
                    player2 = "idk someone"
                    for key2 in range(1, 2):
                        if ctx.author.id != self.bot.games[key][key2]:
                            player2 = self.bot.games[key][key2]
                    await ctx.send(f"{ctx.author.mention} has surrendered! Duel has been won by <@{player2}>.")
                    self.bot.games.pop(ctx.message.channel.id)
            if deterchar == 'N':
                await ctx.send("You are not participating in a duel, so you obviously can't surrender.")
        else:
            await ctx.send("There's no duel running. Can't surrender without being in a duel, can ya?")

def setup(bot):
    bot.add_cog(Duels(bot))