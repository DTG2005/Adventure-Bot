import json
import os
from pathlib import Path

class category:
	def __init__(self, defence, attack, magic):
		self.defence = defence
		self.attack = attack
		self.magic = magic
		
	def dict(self):
		return {'defence': self.defence, 'attack': self.attack, 'magic': self.magic}

class Hunter(category):
	def __init__(self):
		self.category.__init__(10, 15, 20)

class Castellan(category):
	def __init__(self):
		self.category.__init__(15, 15, 15)
	
class Barbarian(category):
	def __init__(self):
		self.category.__init__(25, 15, 5)
		
class Knight(category):
	def __init__(self):
		self.category.__init__(15, 20, 10)
		
class Cleric(category):
	def __init__(self):
		self.category.__init__(5, 10, 25)

class Player(category):
	def __init__(self, name, lvl = 0, money = None, experience = None):
		self.lvl = lvl
		self.name = name
		self.money = 0
		self.category = category
		self.inventory = {}
		self.defence
		self.attack
		self.magic
		
	def diction(self):
		return {'name': self.name, 'info' :{'level': self.lvl, 'money': self.money, 'category': self.category.dict(self), 'inventory': self.inventory}}
			
def UserCheck(name):
	if os.path.getsize('data.json') == 0:
		return True
	else:
		with open('data.json', 'r') as database:
			data = json.load(database)
			for p in data:
				if p['name'] == name:
					return False

def jsonLoad(dict):
	with open('data.json', 'w') as database:
		json.dump(dict, database)
	