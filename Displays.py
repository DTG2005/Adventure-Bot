from discord.ext import commands
import discord
import class_descriptions
import newfile
import sqlite3
import random

categlist = ["Cleric", "Knight", "Barbarian", "Castellan", "Hunter"]

class Displays(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def intro(self, ctx):
		await ctx.channel.send('Hello, thank you for adding me to your server. I am a bot framework specially made for playing games with people, especially RPG ones. \n You may start playing rn or do the ```--help``` to get the help prompt.')
	
	#The entirety of this command is self-explanatory
	@commands.command()
	async def classinfo(self, ctx, vclass):
		if vclass in categlist:
			embedVar = discord.Embed(title=vclass, description = class_descriptions.categdesc[vclass], color = discord.Colour.blue())
			embedVar.add_field(name="Tip", value = random.choice(class_descriptions.categtip[vclass]), inline = False)
			await ctx.send(embed=embedVar)
		else:
			await ctx.send(f'{vclass} is not a suitable class. Try any one of {categlist[0]}, {categlist[1]}, {categlist[2]}, {categlist[3]}, or {categlist[4]}.')


	@commands.command()
	async def stats(self, ctx,*, member: discord.Member = None):
		if member is None:
			try:
				c = self.bot.conn.cursor()
				c.execute('SELECT category, level, money, experience, defence, attack, magic, mainItem FROM UserCredentials WHERE name = (?)', (ctx.author.name,))
				data = c.fetchall()
				category = data [0][0]
				level = int(data[0][1])
				money = int(data[0][2])
				experience = int(data[0][3])
				defence = int(data[0][4])
				attack = int(data[0][5])
				magic = int(data[0][6])
				mainItem = data[0][7]
				embedVar = discord.Embed(title = ctx.author.name, description = f'You are a {category} and currently stand at Level {level} with {experience} experience. You have {money} money.\n\nDefence:{defence}\nAttack:{attack}\nMagic:{magic}\nYour main weapon right now is {mainItem}.')
				embedVar.set_author(name= ctx.author.name, icon_url=ctx.message.author.avatar_url)
				await ctx.send(embed = embedVar)
			except:
				await ctx.send("You haven't joined yet. Try joining now!")
		else:
			c = self.bot.conn.cursor()
			c.execute('SELECT category, level, money, experience, defence, attack, magic, mainItem FROM UserCredentials WHERE name = (?)', (member.name,))
			data = c.fetchall()
			category = data [0][0]
			level = int(data[0][1])
			money = int(data[0][2])
			experience = int(data[0][3])
			defence = int(data[0][4])
			attack = int(data[0][5])
			magic = int(data[0][6])
			mainItem = data[0][7]
			embedVar = discord.Embed(title = member.name, description = f'You are a {category} and currently stand at Level {level} with {experience} experience. You have {money} money.\n\nDefence:{defence}\nAttack:{attack}\nMagic:{magic}\nYour main weapon right now is {mainItem}.')
			embedVar.set_author(name= member.name, icon_url=member.avatar_url)
			await ctx.send(embed = embedVar)

	@commands.command(aliases=['craftables'])
	async def craftable(self, ctx, *, ItemName = None):
		if ItemName is None:
			desc = ""
			for craft in class_descriptions.Craftables:
				desc += f"**{craft}**\n\n"
			embedVar2 = discord.Embed(title = "Craftable Items", description = desc)
			await ctx.send(embed= embedVar2)

		else:
			try:
				embedVar = discord.Embed(title = ItemName, description = class_descriptions.Craftables[ItemName]["Description"], colour = discord.Color(value=int(class_descriptions.rarityColour[class_descriptions.Craftables[ItemName]["Rarity"]], 16)))
				for key in class_descriptions.Craftables[ItemName]:
					if key != "Description":
						embedVar.add_field(name = key, value = class_descriptions.Craftables[ItemName][key])
				await ctx.send(embed = embedVar)
			except:
				await ctx.send("Item not found!!")


	@commands.command()
	async def collectible(self, ctx, itemName = None):
		collectibleList = ["Wood", "Iron", "Amethyst", "Silver", 'Electrum',"Gold", "Petronacium", "Zyber", "Oharium"]
		if itemName is not None:
			if itemName in collectibleList:
				embedVar = discord.Embed(title = itemName, description = class_descriptions.collectibleDesc[itemName][0], colour = discord.Color(value=int(class_descriptions.rarityColour[class_descriptions.collectibleDesc[itemName][1]], 16)))
				embedVar.add_field(name = "Rarity",  value = class_descriptions.collectibleDesc[itemName][1])
				await ctx.send(embed = embedVar)
			else:
				embedVar =discord.Embed(title = "Collectible not found!", description = "The collectible you were looking for was not found. Try one of the following:-", color = discord.Color(value = int("ff0000", 16)))
				for stuff in collectibleList:
					embedVar.add_field(name=stuff, value = class_descriptions.collectibleDesc[stuff][1], inline = False)
				await ctx.send(embed = embedVar)
		else:
			desc = ""
			for collect in collectibleList:
				desc += f'**{collect}**\n\n'
			embed2 = discord.Embed(title = "Collectible Items", description = desc, colour = discord.Color(value=int('00ff00', 16)))
			await ctx.send(embed= embed2)
	
	@commands.command()
	async def moves(self, ctx, *, ItemName = None):
		if ItemName is None:
			c = self.bot.conn.cursor()
			try:
				#Get data from the db
				categ = newfile.getCateg(ctx.author.name, c, self.bot.conn)
				data1 = newfile.getInventory(c, self.bot.conn, ctx.author.name)
				
				embed1 = discord.Embed(title = "Moves" , description = "The moves available for you are listed below", color = discord.Color(value= int("ff8700", 16)))
				embed1.set_author(name= ctx.author.name, icon_url=ctx.message.author.avatar_url)
				for key in data1:
					movedict = class_descriptions.Move_Dict[key[0]]
					for key2 in movedict:
						embed1.add_field(name= key2, value=class_descriptions.Move_Dict[key[0]][key2])
				for move in class_descriptions.DefaultMovesets[categ]:
					embed1.add_field(name= move, value= class_descriptions.DefaultMovesets[categ][move])
				await ctx.send(embed= embed1)

			except sqlite3.Error as error:
				await ctx.send("You have either not joined, or do not have any craftable in Inventory.")
				print(error)
		
		else:
			embed1 = discord.Embed(title = ItemName, description = "The moves for the given equipment are listed below", color = discord.Color(value= int("ff8700", 16)))
			for key in class_descriptions.Move_Dict[ItemName]:
				embed1.add_field(name= key, value= class_descriptions.Move_Dict[ItemName][key])

			await ctx.send(embed = embed1)


	@commands.command()
	async def inventory(self, ctx, member: discord.Member = None):
		if member is None:
			member = ctx.author
			
		c = self.bot.conn.cursor()
		try:
			data1 = newfile.collectibleInventory(c, self.bot.conn, member.name)
			embedVar = discord.Embed(title = member.name , description = "Your inventory contains the following items:-")
			for collectible in data1:
				embedVar.add_field(name = collectible[0], value = collectible[1])
			await ctx.send(embed = embedVar)
		except:
			await ctx.send("You don't have any collectible in your inventory. You can do --mine per 30 minutes to collect some.")

	@commands.command()
	async def effect(self, ctx, effect):
		Embed = discord.Embed(title = effect, description = class_descriptions.effects[effect])
		await ctx.send(embed= Embed)

	@commands.command()
	async def moveset(self, ctx):
		c = self.bot.conn.cursor()

		movesetDat = newfile.getMoveset(c, ctx.author.name)
		categdat = newfile.getCateg(ctx.author.name, c, self.bot.conn)

		try:
			MovesetEmbed = discord.Embed(title= "Moves")
			MovesetEmbed.set_author(name=ctx.author.name, icon_url=ctx.message.author.avatar_url)
			for move in movesetDat[0]:
				if move in class_descriptions.DefaultMovesets[categdat]:
					MovesetEmbed.add_field(name= move, value= class_descriptions.DefaultMovesets[categdat][move])

				for equipment in class_descriptions.Move_Dict:
					if move in class_descriptions.Move_Dict[equipment]:
						MovesetEmbed.add_field(name= move, value= class_descriptions.Move_Dict[equipment][move])

			await ctx.send(embed=MovesetEmbed)
		except sqlite3.Error as error:
			await ctx.send("Error encountered!")
			print(error)

def setup(bot):
    bot.add_cog(Displays(bot))