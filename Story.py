import discord
from discord.ext import commands
import newfile
import asyncio
import lore_data
import sqlite3

class Story_Mode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()

    @commands.command()
    async def storycampaign(self, ctx):
        try:
            self.c.execute('SELECT category FROM UserCredentials WHERE name = (?)', (ctx.author.name,))
            data = self.c.fetchall()
            category = data[0][0]	
        except sqlite3.Error as e:
            await ctx.send("It doesn't seem like you have joined yet. Run ```--join <category>``` to join.")
            print (e)
            return 
        
        ProgressText = ""
        ResponseChar = ""
        Story = ""
        Progress = newfile.getStoryProgress(self.c, ctx.author.name)
        for _ in lore_data.LoreCharConverter:
            if Progress in lore_data.LoreCharConverter[_]:
                ProgressText = _

        LoadingEmbed = discord.Embed(title = "Story Mode", description = ProgressText)
        LoadingEmbed.add_field(name="Are you ready for this? Note: If you abandon the progress before a checkpoint your progress will be lost.", value= ":one: Proceed \n:two: Cancel")

        load = await ctx.send(embed = LoadingEmbed)

        deterchar = ""

        def check(m):
            return m.author.id == ctx.author.id and m.content in ["1", "2"] and m.channel.id == ctx.channel.id
        
        try:
            message = await self.bot.wait_for("message", timeout = 30, check = check)

            if message.content == "1":
                deterchar = "Y"
                ResponseChar = message.content
            elif message.content == "2":
                deterchar = "N"
        
        except asyncio.TimeoutError:
            deterchar = "N"

        if deterchar == "N":
            await ctx.send("Very well then, we shall continue some other time.")
        else: 
            emb = discord.Embed(title = "Story Mode", description = ProgressText)
            emb.add_field(name = "Story", value= lore_data.Lore[Progress][category][int(ResponseChar)])
            await ctx.send(embed= emb)
            await ctx.send(lore_data.LoreResponses[Progress][category][int(ResponseChar)])
            
#            def check(m):
#                return m.author.id == ctx.author.id and m.contnet in 

def setup(bot):
    bot.add_cog(Story_Mode(bot))