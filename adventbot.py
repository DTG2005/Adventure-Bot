import discord
from discord.ext import commands
import newfile
import class_descriptions
import random
import sqlite3
		
def read_token ():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()
		
token = read_token()
AdventBot = commands.Bot(command_prefix = '--')

categlist = ["Cleric", "Knight", "Barbarian", "Castellan", "Hunter"]

@AdventBot.event
async def on_ready():
	print('Let\'s do this')
	
@AdventBot.command()
async def intro(ctx):
	await ctx.channel.send('Hello, thank you for adding me to your server. I am a bot framework specially made for playing games with people, especially RPG ones. \n You may start playing rn or do the ```--help``` to get the help prompt.')

@AdventBot.command()
async def join(ctx, category):
	conn = sqlite3.connect('database.db')
	conn.execute("PRAGMA foreign_keys = 1")
	c = conn.cursor()
	newfile.create_table(conn, c)
	if category in categlist:
		categdict = {'Cleric': [5, 10, 25], 'Knight': [15, 20, 10], 'Barbarian': [15, 15, 15], 'Castellan': [25, 15, 5], 'Hunter': [10, 15, 20]}
		categitem = {'Cleric': 'Broken_Staff', 'Knight': 'Stone Crudesword', 'Barbarian': 'Wooden Mace', 'Castellan': 'Stone Gauntlet', 'Hunter': 'Wooden Bow'}
		try:
			newfile.data_entry(c, ctx.author.name, category, 0, 0, 0, categdict[category], categitem[category], conn)
			await ctx.send(f'You have joined the Adventure as {ctx.author.name}, a {category}.\nYou stand at level 0 and have 0 money. Let the adventure begin!!!')
		except sqlite3.Error as error:
			await ctx.send('You have already joined! You need not join again.')
			
	else:
		await ctx.send(f'{category} is not a valid category. Try joining as {categlist[0]}, {categlist[1]}, {categlist[2]}, {categlist[3]}, or {categlist[4]}.')
	
@AdventBot.command()
async def classinfo(ctx, vclass):
	if vclass in categlist:
		embedVar = discord.Embed(title=vclass, description = class_descriptions.categdesc[vclass], color = discord.Colour.blue())
		embedVar.add_field(name="Tip", value = random.choice(class_descriptions.categtip[vclass]), inline = False)
		await ctx.send(embed=embedVar)
	else:
		await ctx.send(f'{vclass} is not a suitable class. Try any one of {categlist[0]}, {categlist[1]}, {categlist[2]}, {categlist[3]}, or {categlist[4]}.')

@AdventBot.command()
async def campaign(ctx):
	conn = sqlite3.connect('database.db')
	conn.execute("PRAGMA foreign_keys = 1")
	c = conn.cursor()
	try:
		c.execute('SELECT category, level  FROM UserCredentials WHERE name = (?)', (ctx.author.name,))
		data = c.fetchall()
		categ = data[0][0]
		level = data[0][1]
	except:
		await ctx.send('You don\'t seem to have joined. You can do --join "category" now to do so.')
	exp = random.randint(class_descriptions.level_exp_list[str(level)][0], class_descriptions.level_exp_list[str(level)][1])
	newfile.campaign_update(ctx.author.name, c, exp, conn)
	await ctx.send(f'{exp} experience received!!!')
	
		
	
AdventBot.run(token)