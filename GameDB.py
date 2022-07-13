import sqlite3

conn = sqlite3.connect("gameDB")
c = conn.cursor()


c.execute(''' CREATE TABLE IF NOT EXISTS Score_table (
GAME_ID INTEGER PRIMARY KEY , 
SCORE INTEGER)''')

