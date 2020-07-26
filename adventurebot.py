import discord
from discord.ext import commands
import classes
		
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
	if category in categlist:
		if classes.UserCheck(ctx.author.mention):
			if category == "Cleric":
				Playerx1 = classes.Player(classes.Cleric, ctx.author.mention, 0, 0)
			elif category =="Knight":
				Playerx1 = classes.Player(classes.Knight, ctx.author.mention, 0, 0)
			elif category == "Barbarian":
				Playerx1 = classes.Player(classes.Barbarian, ctx.author.mention, 0, 0)
			elif category == "Castellan":
				Playerx1 = classes.Player(classes.Castellan, ctx.author.mention, 0, 0)
			elif category == "Hunter":
				Playerx1 = classes.Player(classes.Hunter, ctx.author.mention, 0, 0)
			await ctx.send(f'You have joined the Adventure as {ctx.author.mention}, a {Playerx1.category}.\nYou stand at level {Playerx1.lvl} and have {Playerx1.money} money. Let the adventure begin!!!')
			Playerdict = Playerx1.diction()
			classes.jsonLoad(Playerdict)
	else:
		await ctx.send(f'{category} is not a valid category. Try joining as {categlist}.')
	

	
AdventBot.run(token)