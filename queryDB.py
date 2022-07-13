import sqlite3
import pandas as pd
conn = sqlite3.connect("gameDB")
c = conn.cursor()

print("All Data :")
c.execute('''SELECT *
          FROM Score_table ''')

df = pd.DataFrame(c.fetchall(), columns=['   Game Id', '   Score'])
print(df)


print("-------------------------------------")

c.execute('''SELECT MAX(SCORE)
          FROM Score_table ''')

print("The highest Score of the game :")
output = c.fetchone()
for row in output:
    print(row)
