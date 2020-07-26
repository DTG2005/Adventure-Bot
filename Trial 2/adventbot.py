import discord
from discord.ext import commands
import newfile
import sqlite3
		
def read_token ():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()
		
token = read_token()
AdventBot = commands.Bot(command_prefix = '--')

@AdventBot.event
async def on_ready():
	print('Let\'s do this')
	
@AdventBot.command()
async def intro(ctx):
	await ctx.channel.send('Hello, thank you for adding me to your server. I am a bot framework specially made for playing games with people, especially RPG ones. \n You may start playing rn or do the ```--help``` to get the help prompt.')

@AdventBot.command()
async def join(ctx, category):
	categlist = ["Cleric", "Knight", "Barbarian", "Castellan", "Hunter"]
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	newfile.create_table(c)
	if category in categlist:
		await ctx.send(f'You have joined the Adventure as {ctx.author.name}, a {category}.\nYou stand at level 0 and have 0 money. Let the adventure begin!!!')
		if category == "Cleric":
			newfile.data_entry(c, ctx.author.name, category, 0, 0, 0, 5, 10, 25, conn)
		elif category =="Knight":
			newfile.data_entry(c, ctx.author.name, category, 0, 0, 0,15, 20, 10, conn)
		elif category == "Barbarian":
			newfile.data_entry(c, ctx.author.name, category, 0, 0, 0, 15, 15, 15, conn)
		elif category == "Castellan":
			newfile.data_entry(c, ctx.author.name, category, 0, 0, 0, 25, 15, 5, conn)
		elif category == "Hunter":
			newfile.data_entry(c, ctx.author.name, category, 0, 0, 0, 10, 15, 20, conn)
			Playerdict = {'name': ctx.author.mention, 'info': {'level': Playerx1.lvl, 'money': Playerx1.money, 'category': Playerx1.dict(), 'inventory': Playerx1.inventory}}
			classes.jsonLoad(Playerdict)
	else:
		await ctx.send(f'{category} is not a valid category. Try joining as {categlist}.')
	
# use ctx.author.name
	
AdventBot.run(token)