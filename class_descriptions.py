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
"Requirements" : "**Wood** : 3",
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
"Type": "Headgear",
"Requirements": "**Iron**: 4",
"Rarity": "Common",
"Equippable Classes": "All"},

"Ferrum Conduit": {"Description": "An artifact made out of pure iron, which will give your magic an **iron** fist. Get it? No? Anyways...",
"Type:": "Artifact",
"Attack Boost": "3%",
"Magic Boost": "3%",
"Requirements": "**Iron** : 7",
"Rarity": "Common",
"Equippable Classes": "Cleric, Hunter"},

"Sturdy Face Cover": {"Description": "A mask made out of iron is a dream come true for magic users. Who wouldn't want an easy to obtain but powerful protection anyway?",
"Type": "Mask",
"Defence Boost": "2%",
"Magic Boost": "3%",
"Requirements": "**Iron** : 3",
"Rarity": "Common",
"Equippable Classes": "Cleric, Hunter"},

"Silver Staff": {"Description": "Who would not want a good staff made out of the more rare of metals? It's more powerful, offers a deeper connection to magic, and can be shapeshifted to form a mirror to look at your own ugly face.",
"Type": "Staff",
"Attack Boost": "3%",
"Magic Boost": "7%",
"Requirements": "**Silver** : 3",
"Rarity": "Rare",
"Equippable Classes": "Cleric, Hunter"},

"Silver Sword": {"Description": "Used for cleaving Monsters and Humans alike, this good ol' Silver Sword can pack a punch or two. Or rather a slice or a stab. It's upto what you like to go ahead with.",
"Type" : "Sword",
"Attack Boost": "6%",
"Requirements" : "**Silver** : 3",
"Rarity" : "Rare",
"Equippable Classes": "Knight, Castellan"},

"Silver Star": {"Description": "A Silver Mace with spikes? Sike! Spike! You can bash their head in along with some deep pierces using this heavy thing. Packs some heavy punches, making it worth the pain. And the cost of crafting.",
"Type" : "Mace",
"Attack Boost": "8%",
"Requirements" : "**Silver** : 6",
"Rarity" : "Rare",
"Equippable Classes" : "Barbarian, Castellan"},

"Silver Helmet": {"Description": "Of course it is stronger than iron! Oh wait, you didn't know? It's a bit of expert goblin craftsmanship",
"Type" : "Headgear",
"Defence Boost": "4%",
"Requirements": "**Silver** : 4",
"Rarity": "Rare",
"Equippable Classes" : "All"},

"Silver Mask": {"Description": "The shiny mask that lays before you is a magical wonder. Equipping it bestows magical boosts previously unknown to many centuries of mages.",
"Type": "Mask",
"Defence Boost": "3%",
"Magic Boost": "5%",
"Requirements": "**Silver** : 3",
"Rarity": "Rare",
"Equippable Classes": "Cleric, Hunter"},

"Sun's Wrath": {"Description": "When you finally find gold, you know what to do with it. No, it's not buying 23 tonnes of bread. You have to make the best staff you can that can channel the strength of the fire to your advantage to burn your foes to a crisp!",
"Type": "Staff",
"Attack Boost": "8%",
"Magic Boost": "15%",
"Requirements": "**Gold** : 3",
"Rarity" : "Epic",
"Equippable Classes": "Cleric, Hunter"},

"Golden Sword": {"Description": "What's with you and your 'Gold and silver aren't strong enough'? They're stronger than most things around and you should learn to accept it.",
"Type": "Sword",
"Attack Boost": "14%",
"Requirements": "**Gold** : 3",
"Rarity": "Epic",
"Equippable Classes": "Knight, Castellan"},

"Sunstar": {"Description": "Time to show your foes the sun is on our side. Channel the strength of gold with your heavy attack style to wreak havoc on the battlefield.",
"Type": "Mace",
"Attack Boost": "18%",
"Requirements": "**Gold** : 6",
"Rarity": "Epic",
"Equippable Classes": "Barbarian, Castellan"},

"Golden Headpiece": {"Description": "When the going gets yellow, make it shine with your own helmet made of gold!",
"Type": "Headgear",
"Defence Boost": "12%",
"Requirements": "**Gold** : 4",
"Rarity": "Epic",
"Equippable Classes": "All"},

"Mask of Light": {"Description": "The mask that lets you channel the power of light. Gold is closer to the element of light as compared to any other thing existing. So why not use this rather than just memorising it like a nerd?",
"Type": "Mask",
"Defence Boost": "10%",
"Magic Boost": "13%",
"Requirements": "**Gold** : 3",
"Rarity": "Epic",
"Equippable Classes": "Cleric, Hunter"},

"Moon's Wrath": {"Description": "Just like Sun is the celestial body Gold can summon the power of, it's the moon Electrum can use. Cast devastating spells of cold and manipulation with the moon by your side",
"Type": "Staff",
"Attack Boost": "8%",
"Magic Boost": "15%",
"Requirements": "**Electrum** : 3",
"Rarity" : "Epic",
"Equippable Classes": "Cleric, Hunter"},

"Electrum Sword": {"Description": "If Gold and Silver alone are so sturdy, imagine them alloyed. Wait, why imagine when you can craft it?",
"Type": "Sword",
"Attack Boost": "16%",
"Requirements": "**Electrum** : 3",
"Rarity": "Epic",
"Equippable Classes": "Knight, Castellan"},

"Moonstar": {"Description": "When you feel like you want to bash someone to the moon, do not hesitate to grab this. The enemy will surely pass out from the high smashpower of this marvel.",
"Type": "Mace",
"Attack Boost": "18%",
"Requirements": "**Electrum** : 6",
"Rarity": "Epic",
"Equippable Classes": "Barbarian, Castellan"},

"Electrum Headpiece": {"Description": "The strong and damage absorbing Electrum helmet every brave warrior should use to keep their head in one piece if the opponent has a lucky chance to aim for what Thor couldn't.",
"Type": "Headgear",
"Defence Boost": "14%",
"Requirements": "**Electrum** : 4",
"Rarity": "Epic",
"Equippable Classes": "All"},

"Mask of Darkness": {"Description": "The mask that lets you channel the power of darkness. Electrum is closer to the element of darkness as compared to any other thing existing. So why not use this rather...oh wait am I repeating myself?",
"Type": "Mask",
"Defence Boost": "10%",
"Magic Boost": "14%",
"Requirements": "**Electrum** : 3",
"Rarity": "Epic",
"Equippable Classes": "Cleric, Hunter"},

"Staff of Balance": {"Description": "The Staff made out of the legendary Oharium, the magical powers of this staff is beyond imagination. Use its devastating powers to form a fool of anyone who dares even look up at you.",
"Type": "Staff",
"Attack Boost": "17%",
"Magic Boost": "25%",
"Requirements": "**Oharium** : 3",
"Rarity": "Legendary",
"Equippable Classes": "Cleric, Hunter"},

"Excalibur": {"Description": "The Excalibur is one of the many classes of legendary swords that make cutting through any armour look like a knife through cotton. With this sword by your side, you can send entire armies running.",
"Type": "Sword",
"Attack Boost": "30%",
"Requirements": "**Oharium** : 3",
"Rarity": "Legendary",
"Equippable Classes": "Knight, Castellan"},

"Cursed Star": {"Description": "The weapon that can flatten an entire steel wall with a single blow, this mighty mace will surely come in handy for front line combat.",
"Type": "Mace",
"Attack Boost": "37%",
"Requirements": "**Oharium** : 6",
"Rarity": "Legendary",
"Equippable Classes": "Barbarian, Castellan"},

"Helmet of Valour": {"Description": "The strongest helmet class used by the Warriors of Valour, the glimmer of light reflected off this helmet sends sparks of fear flying in the heart of your foes. It creates a healing aura while absorving your damage.",
"Type": "Headgear",
"Defence Boost": "25%",
"Requirements": "**Oharium** : 4",
"Rarity": "Legendary",
"Equippable Classes": "All"},

"Mask of Hope": {"Description": "Used by the legendary Warriors of Hope, this legendary mask will provide you with a larger array of spells along with a protective healing aura.",
"Type": "Mask",
"Defence Boost": "20%",
"Magic Boost": "24%",
"Requirements": "**Oharium** : 3",
"Rarity": "Legendary",
"Equippable Classes": "Cleric, Hunter"}}


Crafting_Dict = { "Wooden Staff": {"Wood" : 3}, "Wooden Sword": {"Wood": 5}, "Wooden Mace": {"Wood": 6}, "Wooden Helmet": {"Wood": 3}, "Wooden Mask": {"Wood": 2}, 
"Iron Sword": {"Iron":3}, "Iron Club": {"Iron":4}, "Iron Helmet": {"Iron":4}, "Ferrum Conduit": {"Iron": 7}, "Sturdy Face Cover": {"Iron":3},
"Silver Staff": {"Silver": 3}, "Silver Sword": {"Silver": 3}, "Silver Star": {"Silver": 6}, "Silver Helmet": {"Silver": 4}, "Silver Mask": {"Silver":3},
"Sun's wrath":{"Gold": 3}, "Golden Sword":{"Gold":3}, "Sunstar": {"Gold": 6}, "Golden Headpiece": {"Gold": 4}, "Mask of Light": {"Gold":3}, 
"Moon's Wrath": {"Electrum":3}, "Electrum Sword":{"Electrum":3}, "Moonstar": {"Electrum":6}, "Electrum Headpiece": {"Electrum":4}, "Mask of Darkness": {"Electrum":3},
"Staff of Balance": {"Oharium":3 }, "Excalibur": {"Oharium": 3}, "Cursed Star": {"Oharium": 6}, "Helmet of Valour": {"Oharium":4}, "Mask of Hope": {"Oharium":3}}

Move_Dict = {
	"Wooden Staff": {
		"Whirlwind": "Casts a weak wind slash, dealing 2 damage.",
		"Earth's Vengeance": "Casts a weak shockwave on the ground. Deals 3 damage and surpasses blocks, but requires a cooldown of 1 move."
	},
}