import sqlite3

#So here goes nothing
conn = sqlite3.connect('database.db')
c = conn.cursor()
	
def create_table(conn, c):
#	c.execute('CREATE TABLE IF NOT EXISTS Equipped(name TEXT PRIMARY KEY, Headgear TEXT, Armour TEXT, Lower TEXT, Boots TEXT)')
	
	c.execute('CREATE TABLE IF NOT EXISTS Inventory(name TEXT PRIMARY KEY, Iron REAL, Gold REAL, Purple_Dye REAL, Cloth REAL, Head_of_Medusa REAL, Golden_Fleece REAL, Thunderbolt REAL, Heal_Spell REAL, Supersense_Spell REAL, Magic_Spell REAL)')
		
	c.execute('CREATE TABLE IF NOT EXISTS UserCredentials(name TEXT, category TEXT, level TEXT, money REAL, experience REAL, defence REAL, attack REAL, magic REAL, FOREIGN KEY(name) REFERENCES Inventory(name))')
	conn.commit()
	
def data_entry(c, name, category, level, money, experience, statlist, conn):
	c.execute("INSERT INTO Inventory(name, Iron, Gold, Purple_Dye, Cloth, Head_of_Medusa, Golden_Fleece, Thunderbolt, Heal_Spell, Supersense_Spell, Magic_Spell) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (name, 0,0,0,0,0,0,0,0,0,0))
	
	c.execute ("INSERT INTO UserCredentials (name, category, level, money, experience, defence, attack, magic) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, category, level, money, experience, statlist[0], statlist [1], statlist [2]))
	
	
#	c.execute("INSERT INTO Equipped (name, Headgear, Lower, Armour, Boots) VALUES (?,?,?,?,?)", (name, "none", "none", "none", "none"))
	conn.commit()
	