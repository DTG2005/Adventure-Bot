import discord
from discord.ext import commands
import newfile
import class_descriptions
import random
import sqlite3
import asyncio

def read_token ():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()
		
# Read the token
token = read_token()
class AdventBot (commands.Bot):
	def __init__(self):
		super().__init__(
			command_prefix= "--",
			case_insenitive = True,
			self_bot = False,
			activity = discord.Activity(type=discord.ActivityType.listening, name='Your Lovely Voice.'),
		)
		self.games = {}
		self.conn = sqlite3.connect('database.db')	
		self.conn.execute("PRAGMA foreign_keys = 1")	

		self.load_extension("Displays")
		self.load_extension("Misc")
#		self.load_extension("Duels")
		self.load_extension("Roleplay")

	#So that we know when our sweet bot is ready
	async def on_ready(self):
		print('Let\'s do this')

if __name__ == "__main__":
	AdventBot().run(token)