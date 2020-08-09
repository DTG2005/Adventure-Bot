import sqlite3

#So here goes nothing
conn = sqlite3.connect('database.db')
c = conn.cursor()
	
def create_table(conn, c):
	c.execute('CREATE TABLE IF NOT EXISTS Equipped(name TEXT PRIMARY KEY, Headgear TEXT, Armour TEXT, Lower TEXT, Boots TEXT)')
	
	c.execute('CREATE TABLE IF NOT EXISTS Items(item_name TEXT PRIMARY KEY, type TEXT, subtype TEXT)')
	
	c.execute('CREATE TABLE IF NOT EXISTS Inventory(name TEXT, item_name TEXT, number_held INTEGER, FOREIGN KEY(item_name) REFERENCES Items(item_name))')

	c.execute('CREATE TABLE IF NOT EXISTS Collectibles (name TEXT, collectible TEXT, number_held INTEGER, UNIQUE (name, collectible))')
				
	c.execute('CREATE TABLE IF NOT EXISTS UserCredentials(name TEXT, category TEXT, level TEXT, money INTEGER, experience INTEGER, defence INTEGER, attack INTEGER, magic INTEGER, mainItem TEXT, FOREIGN KEY (name) REFERENCES Equipped(name))')
	conn.commit()
	
def data_entry(c, name, category, level, money, experience, statlist, mainItem, conn):
	c.execute("INSERT INTO Equipped (name, Headgear, Lower, Armour, Boots) VALUES (?,?,?,?,?)", (name, "none", "none", "none", "none"))
		
	c.execute ("INSERT INTO UserCredentials (name, category, level, money, experience, defence, attack, magic, mainItem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, category, level, money, experience, statlist[0], statlist [1], statlist [2], mainItem))
	conn.commit()

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

def get_camp_info(name, c, level, categ):
	c.execute('SELECT category, level  FROM UserCredentials WHERE name = (?)', (name,))
	data = c.fetchall()
	categ = data[0][0]
	level = data[0][1]

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
	c.execute("SELECT number_held FROM Collectibles WHERE (name, collectible) = (?,?)", (name, item))
	data = c.fetchall()
	return data
	
def collectibleUpdate(conn, c, name, item, numb):
	c.execute("UPDATE Collectibles SET number_held = (?) WHERE (name, collectible) = (?,?)", (numb, name, item))
	conn.commit()