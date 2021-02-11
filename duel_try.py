import discord
from discord.ext import commands
from discord import User
import newfile
import class_descriptions
import random
import sqlite3

conn = sqlite3.connect('database.db')	
conn.execute("PRAGMA foreign_keys = 1")	
def read_token ():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()
		
# Read the token
token = read_token()
AdventBot = commands.Bot(command_prefix = '--')

#Initializing a list of currently running battles
BattleList = []

@AdventBot.command()
async def duel(ctx, opponent: User):

	if (ctx.author not in BattleList) and (opponent not in BattleList):
		BattleList.append(opponent)
		BattleList.append(ctx.author)
	
		#Fetch the stats
		try:
			c = conn.cursor()
			c.execute('SELECT category, level, money, experience, defence, attack, magic, mainItem FROM UserCredentials WHERE name = (?)', (ctx.author.name,))
			data = c.fetchall()
			category1 = data [0][0]
			level1 = int(data[0][1])
			defence1 = int(data[0][4])
			attack1 = int(data[0][5])
			magic1 = int(data[0][6])
			mainItem1 = data[0][7]

		#Will return an error if username in database nonexistent (Like my life), so we'll exploit it to return the "haven't joined" error.
		except:
			await ctx.send(f"You haven't joined yet {ctx.author.mention}. Try joining now!")
			return
		try:
			c = conn.cursor()
			c.execute('SELECT category, level, money, experience, defence, attack, magic, mainItem FROM UserCredentials WHERE name = (?)', (opponent.name,))
			data = c.fetchall()
			category2 = data [0][0]
			level2 = int(data[0][1])
			defence2 = int(data[0][4])
			attack2 = int(data[0][5])
			magic2 = int(data[0][6])
			mainItem2 = data[0][7]

		#Here we go again
		except:
			await ctx.send(f"You haven't joined yet {opponent.mention}. Try joining now!")
			return

		def check(author):
			def innerCheck(message):
				return message.author == author and message.content == ("Yes" or "No")
			return innerCheck

	
		await ctx.send(f"You are a {category1} Level {level1}, with {defence1} Defence, {attack1} Attack and {magic1} Magic. You have equipped {mainItem1} as your main item. \n Your opponent is a {category2} Level {level2} with {defence2} Defence, {attack2} Attack and {magic2} Magic. They have equiped {mainItem2} as their main item. \n \nContinue to the fight? (Send Yes/No).")
		confirmation = await AdventBot.wait_for('message', check=check(ctx.author), timeout= 30)
		if confirmation.content == ("Yes" or "yes"):
			await ctx.send (f"Now the opponent. {opponent.mention} do you want to dueal? (Write Yes or No)")
			confirmation1 = await AdventBot.wait_for('message', check=check(opponent), timeout= 30)
			if confirmation1.content == ("Yes" or "yes"):
				ctx.send("Let the battle begin!!!")
			else:
				ctx.send("Battle cancelled.")
		else:
			ctx.send("Battle cancelled.")

		BattleList.remove(ctx.author)
		BattleList.remove(opponent)

	else:
		await ctx.send("You are already in a battle! Warriors with ethics don't fight two battles at the same time! Complete the pending duel and try again.")

	await ctx.send("The battle command prompt is over now.")
	

AdventBot.run(token)