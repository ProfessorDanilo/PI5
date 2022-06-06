import sqlite3

connection = sqlite3.connect('meusTestesDanilo.db')

with open('meusTestesDanilo.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("SELECT * FROM ranking ORDER BY pontuacao DESC;")

rows = cur.fetchall()

for row in rows:
    print(row[2])
    print(row[3])


connection.commit()
connection.close()

