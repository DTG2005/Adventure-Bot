import discord
from discord.ext import commands
import newfile
import class_descriptions
import random
import sqlite3
import asyncio

class Duels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def duel(self, ctx, user: discord.Member):
        if ctx.message.channel.id in list(self.bot.games.keys()):
            await ctx.send("Only one duel per channel is allowed.")
        
        for key in self.bot.games:
            if user.id in self.bot.games[key]:
                await ctx.send("Duel failed: Opponent is already in an ongoing duel!")
            elif ctx.author.id in self.bot.games[key]:
                await ctx.send("You can't go into a second duel with an ongoing duel.")
            elif user.id == ctx.author.id:
                await ctx.send("You killed yourself in duel. Wait...you can't, duel somebody else.")

        if user.bot:
            await ctx.send("You can't duel bots, they can kill you with their botrickery!!")
        else:

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

                else:
                    await ctx.send("Request denied! Duel cancelled.")

def setup(bot):
    bot.add_cog(Duels(bot))