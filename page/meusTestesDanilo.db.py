import sqlite3

connection = sqlite3.connect('meusTestesDanilo.db')

with open('meusTestesDanilo.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("SELECT * FROM ranking;")

rows = cur.fetchall()

for row in rows:
    print(row)


connection.commit()
connection.close()

