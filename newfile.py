import sqlite3
import class_descriptions

#So here goes nothing
conn = sqlite3.connect('database.db')
c = conn.cursor()
	
def create_table(conn, c):
	c.execute('CREATE TABLE IF NOT EXISTS Equipped(name TEXT , Headgear TEXT, Armour TEXT, Lower TEXT, Boots TEXT, UNIQUE (name))')
	
	c.execute('CREATE TABLE IF NOT EXISTS Inventory(name TEXT, item_name TEXT, number_held INTEGER, UNIQUE (name, item_name))')

	c.execute('CREATE TABLE IF NOT EXISTS Collectibles (name TEXT, collectible TEXT, number_held INTEGER)')
				
	c.execute('CREATE TABLE IF NOT EXISTS UserCredentials(name TEXT, category TEXT, level TEXT, money INTEGER, experience INTEGER, defence INTEGER, attack INTEGER, magic INTEGER, mainItem TEXT, Unique(name))')
	
	c.execute('CREATE TABLE IF NOT EXISTS Moveset(name TEXT, move1 TEXT, move2 TEXT, move3 TEXT, move4 TEXT, move5 TEXT, passive1 TEXT, passive2 TEXT, standard TEXT, UNIQUE (name))')
	conn.commit()
	
def data_entry(c, name, category, level, money, experience, statlist, mainItem, conn, moves):
	c.execute("INSERT INTO Equipped (name, Headgear, Lower, Armour, Boots) VALUES (?,?,?,?,?)", (name, "none", "none", "none", "none"))

	c.execute("INSERT INTO Moveset (name, move1, move2, move3, move4, move5, passive1, passive2, standard) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, moves[0], moves[1], moves[2], moves[3], moves[4], moves[5], moves[6], "none"))
		
	c.execute ("INSERT INTO UserCredentials (name, category, level, money, experience, defence, attack, magic, mainItem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, category, level, money, experience, statlist[0], statlist [1], statlist [2], mainItem))
	conn.commit()

def getMainEquipment(c, name):
	c.execute("SELECT mainItem FROM UserCredentials WHERE name = (?)", (name,))
	data = c.fetchall()
	return data

def getOtherEquipment(c, name):
	c.execute("SELECT Headgear, Armour, Lower, Boots FROM Equipped WHERE name = (?)", (name,))
	data = c.fetchall()
	return data

def getall(name, c, category, level, money, experience, defence, attack, magic, mainItem):
	c.execute('SELECT category, level, money, experience, defence, attack, magic, mainItem FROM UserCredentials WHERE name = (?)', (name,))
	data = c.fetchall()
	category = data [0][0]
	level = data[0][1]
	money = data[0][2]
	experience = data[0][3]
	defence = data[0][4]
	attack = data[0][5]
	magic = data[0][5]
	mainItem = data[0][6]

def EquipMainItem(name, c, conn, Item):
	c.execute("UPDATE UserCredentials SET mainItem = (?) WHERE name = (?)", (Item, name))
	conn.commit()

def get_camp_info(name, c, level, categ):
	c.execute('SELECT category, level  FROM UserCredentials WHERE name = (?)', (name,))
	data = c.fetchall()
	categ = data[0][0]
	level = data[0][1]

def EquipOtherItems(c, conn, name, item, type1):
	c.execute(f"UPDATE Equipped SET {type1} = (?) WHERE name = (?)", (item, name))
	conn.commit()

def campaign_update(name, c, exp, conn, level):
	c.execute('UPDATE UserCredentials SET experience = (?), level = (?) WHERE name = (?)', (exp, level, name))
	conn.commit()
	
def getCateg(name, c, conn, categ = None):
	c.execute('SELECT category FROM Usercredentials WHERE name = (?)', (name,))
	data = c.fetchall()
	categ = data[0][0]
	return categ
	
def collectibleInsert(c, conn, name, item, number):
	c.execute("INSERT INTO Collectibles(name, collectible, number_held) VALUES(?,?,?)", (name, item, number))
	conn.commit()
	
def collectibleUpdateInfo(c, name, item):
	c.execute("SELECT number_held FROM Collectibles WHERE name = (?) AND collectible = (?)", (name, item))
	data = c.fetchall()
	return data
	
def collectibleUpdate(conn, c, name, item, numb):
	c.execute("UPDATE Collectibles SET number_held = (?) WHERE name = (?) AND  collectible = (?)", (numb, name, item))
	conn.commit()

def getCraftData(c, conn, name, requirement):
	c.execute("SELECT number_held FROM Collectibles WHERE name = ? AND collectible = ?", (name, requirement))
	data = c.fetchall()
	return data

def collectibleInventory(c, conn, name):
	c.execute("SELECT collectible, number_held FROM Collectibles WHERE name = (?)", (name,))
	data = c.fetchall()
	return data
	
def craftableUpdate(c, conn, num, name, craftable):
	c.execute("UPDATE Inventory SET number_held = (?) WHERE name = (?) AND item_name = (?)", (num, name, craftable))
	conn.commit()

def craftableEntry(c, conn, name, craftable):
	c.execute("INSERT INTO Inventory(name, item_name, number_held) VALUES (?,?,1)", (name, craftable))
	conn.commit()
	
def getCraftableData(c, conn, name, craftable):
	c.execute("SELECT number_held FROM Inventory WHERE name = (?) AND item_name = (?)", (name, craftable))
	data = c.fetchall()
	return data

def getInventory(c, conn, name):
	c.execute("SELECT item_name, number_held FROM Inventory WHERE name = (?)", (name,))
	data = c.fetchall()
	return data
	
def updateCraftable(c, conn, num, name, craftable):
	c.execute("UPDATE Inventory SET number_held = (?) WHERE name = (?) AND item_name = (?)", (num, name, craftable))
	conn.commit()

def getMoveset(c, name):
	c.execute("SELECT move1, move2, move3, move4, move5, passive1, passive2, standard FROM Moveset WHERE name = (?)", (name,))
	data = c.fetchall()
	return data