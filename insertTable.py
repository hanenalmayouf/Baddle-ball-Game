import sqlite3
conn = sqlite3.connect('gameDB')
c = conn.cursor()

c.execute('''
INSERT INTO Score_table VALUES 
(1,50),
(2,20),
(3,40),
(4,20),
(5,90),
(6,20),
(7,50)''')
conn.commit()
