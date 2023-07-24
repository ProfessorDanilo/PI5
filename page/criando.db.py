import sqlite3

connection = sqlite3.connect('dados.db')

with open('salvando_dados.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

#cur.execute("SELECT * FROM ranking ORDER BY pontuacao DESC;")

connection.commit()
connection.close()

