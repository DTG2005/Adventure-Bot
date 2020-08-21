import random

categdesc = {'Cleric': 'A Cleric is a Powerful wizard adept in many arts, light and dark alike. His sorcery has greatly reduced his physical strength, but he still stands undefeated in his magical feats. If nothing, he can still entertain your children with his tricks of pulling carrots from a nose.\n\nDefence Base Value: 5\nAttack Base Value: 10\nMagic Base Value: 25',
		 'Knight': 'A Knight is a pure warrior, a race of humans focused on fighting with a moral intent. They have never seen defeat, for they would choose an honourable death over it anyday. However, they don\'t speak much, which is why you\'re never sure if they\'re really warriors or robots.\n\nDefence Base Value: 15\nAttack Base Value: 20\nMagic Base Value: 10',
		  'Barbarian': 'Barbarians, like their names, are plain barbarians. No really, they are just wild warriors who have come to naturally master the arts of survival, giving them a completely balanced control over their Physical as well as Magical strengths. But they\'re known to be a little grumpy so do take care.\n\nDefence Base Value: 15\nAttack Base Value: 15\nMagic Base Value: 15',
		   'Castellan': 'A Castellan is a very special class as it has a certain beneficial bias over defence. As the king\'s representative, he wears so much armour he himself feels unbalanced if he takes it off. However, his lack of quick magic skills are covered up by his huge defence, which makes him a total tank.\n\nDefence Base Value: 25\nAttack Base Value: 15\nMagic Base Value: 5' ,
		    'Hunter': 'A hunter is a being that lives in the nature to practice denunciation. He is more like a monk, but still retains his warrior skills. His strong spiritual powers make him quite powerful in wizardry without compromising on attack or defence.\n\nDefence Base Value: 10\nAttack Base Value: 15\nMagic Base Value: 20'}

categtip = {'Cleric': ['Don\'t try to take a lot of risk; you\'re terribly fragile!',
		'Avoid frontline combat, rather use magical tricks.',
		'A Cleric can only equip robes, which barely grant defences but do offer significant magical boosts!',
		'Try poking your nose less, those carrots might fall before the show.'],
		'Knight': ['You have a good attack, use it well to ambush your opponents.',
		'The Knight is a robot with a human face. **Always remember that.**',
		'Be sure to dodge some magical attacks or they will do some nice damage.',
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

		
Categ_determiner = {'Cleric': 'c',
'Hunter': 'h',
'Knight': 'k',
'Barbarian': 'b',
'Castellan': 'ca'}

level_exp_list = { '0': [5, 20],
'1': [10, 30],
'2': [15, 40],
'3': [20, 50],
'4': [25, 60],
'5': [30, 70]}

def lvl_dict(dict1, level, exp):
	if level >= 0:
		dict1['c'].append(f'You went out to resesrch on some magical herbs. You found a handful of some, which the children took away, and {exp} experience.')
		dict1['c'].append(f'You tried your magic on the wooden pole. You got {exp} experience.')
		dict1['h'].append(f'You meditated besides the waterfall. You got {exp} experience.')
		dict1['h'].append(f'You hunted a bear with your magic. Uou got {exp} experience.')
		dict1['b'].append(f'You practiced by swinging that mace of yours around. You got {exp} experience.')
		dict1['b'].append(f'You lit a fire and roasted a turkey. A hyena tried snatching your fill but you killed it and took him as your fill too. You got {exp} experience.')
		dict1['k'].append(f'You practiced your march. You got {exp} experience.')
		dict1['k'].append(f'You swing that sword ferociously, beheading the imaginary dragon. You get an imaginary dragon\'s tooth and {exp} experience.')
		dict1['ca'].append(f'You practiced punching with your gauntlet. You gained {exp} experience.')
		dict1['ca'].append(f'You tried reasoning with the local gang\'s henchmen. They were threatened and ran away, while you earned {exp} experience.')
		
	if level>=1:
		dict1['c'].append(f'You tried conjuring a wand out. You got {exp} experience.')
		dict1['c'].append(f'You ventured into the wild to gather some plants for a ritual. The ritual provided you with {exp} experience.')
#		dict1[]
		
	return dict1

collectibleDesc = { "Wood": ("This is the basic material all adventurers start with. It is so common infact you can find it in your backyard.", "Common"),
 "Iron": ("Found with easily, this material is what everyone would use for a good brush up weapon. Equipment made from it are durable but sometimes weak.", "Common"),
 "Amethyst": ("Also known as the purple stone of doom, this gemstone is priced by wizards for its rarity and magical powers.", "Rare"),
 "Silver": ("Only the most skilled craftspeople know that Silver can be used for more intricate weaponry and armoury. This fragile metal when handled in the right way can be the perfection for a right warrior, and a power boost for a wizard.", "Rare"),
 "Gold": ("The shining yellow metal every living being covetes, but few know its true usage. This metal makes the difference between a kill and a death.", "Epic"),
 "Electrum": ("The mixture of Gold and Silver gives you the mighty Electrum. Mightier than the mightiest steel swords, this can be a fatal metal for your enemies.", "Epic"),
 "Petronacium": ("The coveted Red coloured gemstone of the distant lands, this stone is what the most skilled sorcerors use in their endeavours. You shall be more than just lucky to find these.", "Epic"),
 "Zyber": ("The mythical yellow gemstone that is known to bestow unparalleled magical powers to the wielder. Using this in your equipment could make you nothing less than a God.", "Legendary"),
 "Oharium": ("The pale green metal known only to a few, this metal is so precious you can buy an entire kingdom with just a bar. And so strong it can make a warrior stronger than an army of thousands.", "Legendary") }
 
rarityColour = {"Common": 'a5a5a5', "Rare": '0093ff', "Epic": '9e00ff', "Legendary": 'f1e100'}

def itemRarity():
	if random.randint(0, 40) == 1:
		return 'Legendary'
	elif random.randint(0, 10) == 1:
		return 'Epic'
	elif random.randint(0, 10) < 4:
		return 'Rare'
	else:
		return 'Common'

rarityItemRandom = { "Common": [1, 10], "Rare": [1, 5], "Epic": [1, 3], "Legendary": [1, 2]}

Items = {'Common': ['Wood', 'Iron'], 'Rare': ['Amethyst', 'Silver'], 'Epic': ['Gold', 'Petronacium'], 'Legendary': ['Zyber', 'Oharium']}

Craftables = {"Wooden Staff": {"Description": "This is a random wooden staff. Nothing magical. You should doubt if it even casts spells hah!",
"Type":"Staff",
"Attack Boost":"2%",
"Magic Boost":"1%",
"Requirements" : "Wood : 3",
"Rarity" : "Common", 
"Equippable Classes":"Cleric, Hunter"},

"Wooden Sword": {"Description":"This wooden sword has nothing special except lightness and somewhat sharpness.",
"Type":"Sword",
"Attack Boost":"2%",
"Requirements": "**Wood**: 5",
"Rarity":"Common",
"Equippable Classes":"Castellan, Knight"},

"Wooden Mace": {"Description": "This is basically a clublike weapon made out of wood with a basic boost to attacks.", 
"Attack boost": "3%", 
"Type": "Mace",
"Requirements": "**Wood**:6", 
"Rarity" : "Common",
"Eqippable Classes":  "Barbarian, Castellan"},

"Wooden Helmet": {"Description": "The helmet made out of wood. Can be chopped as easily as wood.",
"Defence boost":"3%",
"Type": "Headgear",
"Requirements": "**Wood**: 3",
"Rarity": "Common",
"Equippable Classes": "All"},

"Wooden Mask":{"Description" : "The mask made out of wood. It does give a small boost to magic, but nearly no defence boost at all.",
"Defence Boost": "1%",
"Magic Boost": "2%",
"Type": "Mask",
"Requirements": "**Wood**: 2",
"Rarity": "Common",
"Equippable Classes": "Cleric, Hunter"},

"Iron Sword": {"Description": "Do not be deceived by how easy it is to craft it. It is a sturdy and powerful starter weapon.",
"Attack Boost" : "3%",
"Type": "Sword",
"Requirements": "**Iron**: 3",
"Rarity": "Common",
"Equippable Classes": "Knight, Castellan"},

"Iron Club": {"Description": "Perhaps a little rusty, this club actually is a good weapon for flattening your enemy's curves.",
"Attack Boost": "5%",
"Type": "Mace",
"Requirements": "**Iron**: 4",
"Rarity": "Common",
"Equippable Classes": "Barbarian, Castellan"},

"Iron Helmet": {"Description": "An iron helmet is the perfect helmet for a fitting warrior.",
"Defence Boost": "3%",
"Type": "Helmet",
"Requirements": "**Iron**: 4",
"Rarity": "Common",
"Equippable Classes": "All"}}

Crafting_Dict = { "Wooden Staff": {"Wood" : 3}}