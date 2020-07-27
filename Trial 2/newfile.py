import sqlite3

#So here goes nothing
conn = sqlite3.connect('database.db')
c = conn.cursor()
	
def create_table(c):
	c.execute('CREATE TABLE IF NOT EXISTS UserCredentials(name TEXT, category TEXT, level TEXT, money REAL, experience REAL, defence REAL, attack REAL, magic REAL)')
	
def data_entry(c, name, category, level, money, experience, defence, attack, magic, conn):
	c.execute ("INSERT INTO UserCredentials (name, category, level, money, experience, defence, attack, magic) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, category, level, money, experience, defence, attack, magic))
	conn.commit()

