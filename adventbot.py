import discord
from discord.ext import commands
import newfile
import random
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
	conn.execute("PRAGMA foreign_keys = 1")
	c = conn.cursor()
	newfile.create_table(conn, c)
	if category in categlist:
		await ctx.send(f'You have joined the Adventure as {ctx.author.name}, a {category}.\nYou stand at level 0 and have 0 money. Let the adventure begin!!!')
		categdict = {'Cleric': [5, 10, 25], 'Knight': [15, 20, 10], 'Barbarian': [15, 15, 15], 'Castellan': [25, 15, 5], 'Hunter': [10, 15, 20]}
		newfile.data_entry(c, ctx.author.name, category, 0, 0, 0, categdict[category], conn)
	else:
		await ctx.send(f'{category} is not a valid category. Try joining as {categlist[0]}, {categlist[1]}, {categlist[2]}, {categlist[3]}, or {categlist[4]}.')
	
@AdventBot.command()
async def classinfo(ctx, vclass):
	categlist = ["Cleric", "Knight", "Barbarian", "Castellan", "Hunter"]
	if vclass in categlist:
		categdesc = {'Cleric': 'A Cleric is a Powerful wizard adept in many arts, light and dark alike. His sorcery has greatly reduced his physical strength, but he still stands undefeated in his magical feats. If nothing, he can still entertain your children with his tricks of pulling carrots from a nose.\n\nDefence Base Value: 5\nAttack Base Value: 10\nMagic Base Value: 25',
		 'Knight': 'A Knight is a pure warrior, a race of humans focused on fighting with a moral intent. They have never seen defeat, for they would choose an honourable death over it anyday. However, they don\'t speak much, which is why you\'re never sure if they\'re really warriors or robots.\n\nDefence Base Value: 15\nAttack Base Value: 20\nMagic Base Value: 10',
		  'Barbarian': 'Barbarians, like their names, are plain barbarians. No really, they are just wild warriors who have come to naturally master the arts of survival, giving them a completely balanced control over their Physical as well as Magical strengths. But they\'re known to be a little grumpy so do take care.\n\nDefence Base Value: 15\nAttack Base Value: 15\nMagic Base Value: 15',
		   'Castellan': 'A Castellan is a very special class as it has a certain beneficial bias over defence. As the king\'s representative, he wears so much armour he himself feels unbalanced if he takes it off. However, his lack of quick magic skills are covered up by his huge defence, which makes him a total tank.\n\nDefence Base Value: 25\nAttack Base Value: 15\nMagic Base Value: 5' ,
		    'Hunter': 'A hunter is a being that lives in the nature to practice denunciation. He is more like a monk, but still retains his warrior skills. His strong spiritual powers make him quite powerful in wizardry without compromising on attack or defence.\n\nDefence Base Value: 10\nAttack Base Value: 15\nMagic Base Value: 20'}
		embedVar = discord.Embed(title=vclass, description = categdesc[vclass], color = discord.Colour.blue())
		categtip = {'Cleric': ['Don\'t try to take a lot of risk; you\'re terribly fragile!',
		'Avoid frontline combat, rather use magical tricks.',
		'A Cleric can only equip robes, which barely grant defences but do offer significant magical boosts!',
		'Try poking your nose less, those carrots might fall before the show.'],
		'Knight': ['You have a good attack, use it well to ambush your opponents.',
		'The Knight is a robot with a human face. **Always remember that.**',
		'Be sure to dodge some magical attacks or they will do some nice damage.'
		'Your morality grants you a special aura as long as you maintain your ethics.'],
		'Barbarian': ['My master sometimes fears you won\'t understand a thing, so he put minimal tips for you :stuck_out_tongue:.',
		'Don\'t push it a lot hard, you can take some damage, just be mindful.',
		'You have an upper hand due to your balance, use it well.',
		'Barbarians are unique in the way they can use any armour or robe and still look like a a barbarian. Gross, I meant.'],
		'Castellan': ['You fight for the honour of the king, or rather for your own head.',
		'Your defence is too great to bear. Use yourself as a tank. The enemy could not stsnd it.',
		'The castellan has a heavy armoue for his protection. This is some useful heavy stuff.',
		'The diplomatic adventures might make you richer, depended on how you see them.'],
		'Hunter': ['You live on the energy of the nature dude. You are cool af <:shadysmirk:459055417658441743>.',
		'Use your attack and magic strength to wreak havoc on the battlefield.',
		'Hunter is a pretty balanced class, so try to use it strategically to your benefit',
		'The Hunter can use Cleric\'s equipment, but Cleric cannot use those of Hunter. You got an advantage, dude']}
		embedVar.add_field(name="Tip", value = f'{random.choice(categtip[vclass])}', inline = False)
		await ctx.send(embed=embedVar)
	else:
		await ctx.send(f'{vclass} is not a suitable class. Try any one of {categlist[0]}, {categlist[1]}, {categlist[2]}, {categlist[3]}, or {categlist[4]}.')
	
AdventBot.run(token)