from discord.ext import commands
import random
import asyncio
import discord
import class_descriptions
import lore_data
import sqlite3
import newfile

categlist = ["Cleric", "Knight", "Barbarian", "Castellan", "Hunter"]

class Roleplay(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	#Joining commands so it works well
	@commands.command()
	async def join(self, ctx, category):
		#Database init
		c = self.bot.conn.cursor()
		newfile.create_table(self.bot.conn, c)
		
		#Check if category is in there
		if category in categlist:
			categdict = {'Cleric': [5, 10, 25], 'Knight': [15, 20, 10], 'Barbarian': [15, 15, 15], 'Castellan': [25, 15, 5], 'Hunter': [10, 15, 20]}
			Joinemb = discord.Embed(title = "The Tale of Xandelf", description = "The land of everlasting gloom.")

			tpage = len(lore_data.lore_begin)
			currpage = 1

			Joinemb.add_field(name= lore_data.lore_begin[currpage-1], value=f"page {currpage}/{tpage}")
			message = await ctx.send(embed= Joinemb)


			await message.add_reaction("◀️")
			await message.add_reaction("▶️")
			await message.add_reaction("⏭")

			def check(reaction, user):
				return user == ctx.author and str(reaction.emoji) in ["⏭", "▶️", "◀️"]

			while True:
				reaction, user = await self.bot.wait_for("reaction_add", timeout=3000, check = check)

				if str(reaction.emoji) == "▶️" and currpage != tpage:
					currpage += 1
					Joinemb2 = discord.Embed(title = "The Tale of Xandelf", description = "The land of everlasting gloom.")
					Joinemb2.add_field(name= lore_data.lore_begin[	currpage-1], value=f"page {currpage}/{tpage}")
					await message.edit(embed= Joinemb2)
					await message.remove_reaction(reaction, user)

				elif str(reaction.emoji) == "◀️" and currpage > 1:
					currpage -= 1
					Joinemb2 = discord.Embed(title = "The Tale of Xandelf", description = "The land of everlasting gloom.")
					Joinemb2.add_field(name= lore_data.lore_begin[currpage-1], value=f"page {currpage}/{tpage}")
					await message.edit(embed= Joinemb2)
					await message.remove_reaction(reaction, user)

				elif str(reaction.emoji) == "⏭":
					#Database will return an error if there's an existing instance of the name joined. Thus, I'll exploit this to give back an explanatory response
					try:
						newfile.data_entry(c, ctx.author.name, category, 0, 0, 0, categdict[category], None, self.bot.conn, list(dict.keys(class_descriptions.DefaultMovesets[category])))
						await ctx.send(f'You have joined the Adventure as {ctx.author.name}, a {category}.\nYou stand at level 0 and have 0 money. Let the adventure begin!!!')
						await message.remove_reaction(reaction, user)
					except sqlite3.Error as e:	
						await ctx.send('You have already joined! You need not join again.')			
						print (e)
				else:
					await message.remove_reaction(reaction, user)
		else:
			await ctx.send(f'{category} is not a valid category. Try joining as {categlist[0]}, {categlist[1]}, {categlist[2]}, {categlist[3]}, or {categlist[4]}.')
		

	#The standard Campaign command
	@commands.command()
	@commands.cooldown(1, 1800, commands.BucketType.user)
	async def campaign(self, ctx):
		c = self.bot.conn.cursor()

		#The database will again return an error in case the user has not registered, since the database has no instance of the user name.
		try:
			c.execute('SELECT category, level, experience FROM UserCredentials WHERE name = (?)', (ctx.author.name,))
			data = c.fetchall()
			categ = data[0][0]
			experience = int(data [0][2])
			level = data[0][1]
		except:
			await ctx.send('You don\'t seem to have joined. You can do --join "category" now to do so.')
			
		#everything below this is database gibberish you might want to skip out.
		exp = random.randint(class_descriptions.level_exp_list[str(level)][0], class_descriptions.level_exp_list[str(level)][1])
		experience += exp
		
		dict1 = {'c': [f'You looked in your wizardry books to revise. You got {exp} experience.'], 'h': [f'You practiced hitting the target with your bow. You got {exp} experience.'], 'b':[f'You tried learning the tongue of the civilised. You got {exp} experience.'], 'k':[f'You went to the Priestess of the Church for some "Holy Training". You got {exp} experience.'], 'ca': [f'You reasoned with some traders to reduce the taxes. You succeeded, however getting a handful of curses and {exp} experience']}
		
		dict10 = class_descriptions.lvl_dict(dict1, int(level), exp)
		await ctx.send(random.choice(dict10[class_descriptions.Categ_determiner[categ]]))
		if experience < 2*100*(int(level)+1):
			newfile.campaign_update(ctx.author.name, c, experience, self.bot.conn, level)
		else:
			await ctx.send("Level up!!!")
			newfile.campaign_update(ctx.author.name, c, experience, self.bot.conn, int(level)+1)
		
	@campaign.error
	async def campaign_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Your Character is tired from going on a campaign. Try again after resting {int(error.retry_after/60)} minutes and {int(error.retry_after%60)} seconds.")

	#This too is pretty much self explanatory
	@commands.command()
	@commands.cooldown(1, 900, commands.BucketType.user)
	async def mine(self, ctx):
		try:
			rarity = class_descriptions.itemRarity()[0]
			Item = random.choice(class_descriptions.Items[rarity])
			int1 = random.randint(class_descriptions.rarityItemRandom[rarity][0], class_descriptions.rarityItemRandom[rarity][1])
			woodResponses = {"c": f"After a lot of magical practice you could chop down the small tree in your backyard. You got {int1} wood.",
		"h": f"You smashed down an entire tree using your strength. You got {int1} wood.",
		'b': f"You just gutted an entire tree as if it were some small sapling. You got {int1} wood.",
		'k': f"As the church ordered, you chopped down an unholy tree. The church lets you keep {int1} wood.",
		'ca': f"You ordered your royal servants to chop you some wood. They got you {int1} wood."}

			mineResponses = { "c": f"You mined for an hour and could finally get {int1} {Item}.",
		"h": f"You went into the cave to take whatever mother earth had to offer. You got {int1} {Item}.",
		"b": f"You saw something shiny on the rock and kept hitting it for some minutes. It broke and gave you {int1} {Item}.",
		"k": f"You went into the cave to mine into a vein of {Item}. You found {int1} of it.",
		"ca": f'You ordered your miners to bring you a lot of {Item}. They couldn\'t find a lot there but only {int1}'}
			c = self.bot.conn.cursor()
			try:
				categ = newfile.getCateg(ctx.author.name, c, self.bot.conn)
			except sqlite3.Error:
				ctx.send("You haven't joined yet. Do the join command: --join to join now!!!")
			categChar = class_descriptions.Categ_determiner[categ]
			if Item == "Wood":
				await ctx.send(woodResponses[categChar])
			else:
				await ctx.send(mineResponses[categChar])
			data = newfile.collectibleUpdateInfo(c, ctx.author.name, Item)
			if not data:
				newfile.collectibleInsert(c, self.bot.conn, ctx.author.name, Item, int1)
			else:
				int1 += data[0][0]
				newfile.collectibleUpdate(self.bot.conn, c, ctx.author.name, Item, int1)
		except IndexError:
			await ctx.send("It seems you have not joined yet. Join using the join command to collect your mined reward.")

	@mine.error
	async def mine_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Your Character can only mine once in 15 minutes. You can try again in {int(error.retry_after/60)} minutes and {int(error.retry_after%60)} seconds.")
		if isinstance(error, IndexError):
			await ctx.send("It seems you have not joined yet. Join using the join command to collect your mined reward.")

	#database gibberish you'd want to leave out again
	@commands.command()
	async def craft(self, ctx, *, craftable):
		c = self.bot.conn.cursor()
		if craftable in class_descriptions.Crafting_Dict:
			required = list(class_descriptions.Crafting_Dict[craftable].keys())[0]
			collected = newfile.getCraftData(c, self.bot.conn, ctx.author.name, required)
			if collected:
				if collected[0][0] >= class_descriptions.Crafting_Dict[craftable][required]:
					await ctx.send(f"You have crafted a {craftable}!!")
					collectnum = newfile.getCraftableData(c, self.bot.conn, ctx.author.name, craftable)
					if not collectnum:
						newfile.craftableEntry(c, self.bot.conn, ctx.author.name, craftable)
						newfile.collectibleUpdate(self.bot.conn, c, ctx.author.name, required, collected[0][0] - class_descriptions.Crafting_Dict[craftable][required])
					else:
						collectnum1 = collectnum[0][0]
						collectnum1 += 1
						newfile.updateCraftable(c, self.bot.conn, collectnum1, ctx.author.name, craftable)
						newfile.collectibleUpdate(self.bot.conn, c, ctx.author.name, required, collected[0][0] - class_descriptions.Crafting_Dict[craftable][required])
							
				else:
					await ctx.send(f"You have too less of {required} to craft {craftable}. You should try mining more.")
					
			elif not collected:
				await ctx.send("You don't have any material of this kind. Try collecting some by mining.")
		else:
			await ctx.send("You cannot craft this material.")
				
		
	@commands.command()
	async def equip(self, ctx, *, itemName):
		c = self.bot.conn.cursor()
		#Get data from the database
		try:
			data1 = newfile.getInventory(c, self.bot.conn, ctx.author.name)
		except:
			await ctx.send("Selected item cannot be found. Perhaps try seeing if you can craft it.")
		#Iteration happens here
		for key in data1:
			if key[0] == itemName:
				newItemNum = key[1] - 1
				#Below this I'll update the db since equipment decreases 1 amount from the inventory
				if newItemNum >= 0:
					newfile.updateCraftable(c, self.bot.conn, newItemNum, ctx.author.name, itemName)
					#Now, we can go ahead and check what type of equipment it is so we can equip it in the specified slot
					if class_descriptions.Craftables[itemName]["Type"] in class_descriptions.Main_equipment_dict:
						newfile.EquipMainItem(ctx.author.name, c, self.bot.conn, itemName)
						await ctx.send("Main Item has been equipped!!")
					else:
						newfile.EquipOtherItems(c, self.bot.conn, ctx.author.name, itemName, class_descriptions.Equipment_db_dict[class_descriptions.Craftables[itemName]["Type"]])
						await ctx.send(f"{itemName} has been equipped!!")
				else:
					await ctx.send("Selected Item cannot be found!!")

	@commands.command()
	async def addmove(self, ctx, move):
		if '[p]' in move:
			movetype = "passive"
		else:
			movetype = "normal"
		try:
			c = self.bot.conn.cursor()
			deterchar = 'n'
			#Get data from the db
			data1 = newfile.getMainEquipment(c, ctx.author.name)
			data2 = newfile.getOtherEquipment(c, ctx.author.name)
			movesetData = newfile.getMoveset(c, ctx.author.name)
			NorMove1 = movesetData[0][0]
			NorMove2 = movesetData[0][1]
			NorMove3 = movesetData[0][2]
			NorMove4 = movesetData[0][3]
			NorMove5 = movesetData[0][4]
			PassMove1 = movesetData[0][5]
			PassMove2 = movesetData[0][6]
			Movelist = [NorMove1, NorMove2, NorMove3, NorMove4, NorMove5, PassMove1, PassMove2]

			for move1 in class_descriptions.Move_Dict[data1[0][0]]:
				if  move1 == move:
					deterchar = 'c'
				else:
					for equipment in data2:
						for key in equipment:
							if key != "none":
								movedict = class_descriptions.Move_Dict[key]
								for key2 in movedict:
									if move == key2:
										#Ima do stuff here
										deterchar = 'c'
					
			if deterchar == 'c':
				desc = ""
				await ctx.send("Move is available to be added. Loading prompt.")
				for key in range(0, 7):
					desc += f"{key + 1} = {Movelist[key]}\n"

				ChangemoveEmbed = discord.Embed(title= "Change your moves", description= desc)
				await ctx.send(embed=ChangemoveEmbed)

				def check(m):
					return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id and m.content in ['1', '2', '3', '4', '5', '6', '7']

				try:
					msg = await self.bot.wait_for('message', check= check, timeout= 30.0)
				except asyncio.TimeoutError:
					await ctx.send("Time ran out! Try again!")
					return

				else:
					if movetype == 'normal' and int(msg.content) < 6:
						movesetType = "move"+ msg.content
						newfile.moveUpdate(c, self.bot.conn, ctx.author.name, movesetType, move)
						await ctx.send("Move replaced successfully!")
					elif movetype == 'passive' and int(msg.content) > 5:
						movesetType = "passive"+ str(int(msg.content) - 5)
						newfile.moveUpdate(c, self.bot.conn, ctx.author.name, movesetType, move)
						await ctx.send("Move replaced successfully!")
					else:
						await ctx.send("You can only replace Passives with Passives, and Normals with Normal moves.")
			else:
				await ctx.send("This move is currently unavailable.")

		except sqlite3.Error as error:
			await ctx.send("You have either not joined, or do not have any available Moves.")
			print(error)

def setup(bot):
	bot.add_cog(Roleplay(bot))