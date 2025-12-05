import sqlite3

connection = sqlite3.Connection("Roster11.db")
cursor = connection.cursor()

command1 = "Create table Roster (Name text, Species text, Age integer)"

cursor.execute(command1)

cursor.execute("insert into Roster values ('Benjamin Sisko', 'Human', 40)")
cursor.execute("insert into Roster values ('Jadzia Dax', 'Trill', 300)")
cursor.execute("insert into Roster values ('Kira Nerys', 'Bajoran', 29)")

cursor.execute("select * from Roster")

result = cursor.fetchall()

print(result)

connection.commit()
connection.close()


import sqlite3

connection = sqlite3.Connection("Roster11.db")
cursor = connection.cursor()

cursor.execute("Update Roster set Name = 'Ezri Dax' where Age = 300")
connection.commit()
cursor.execute("select * from Roster")
result = cursor.fetchall()

print(result)

import sqlite3

connection = sqlite3.Connection("Roster11.db")
cursor = connection.cursor()
new_query = cursor.execute("select Name, Age from Roster where Species = 'Bajoran'")

print(new_query.fetchall())


