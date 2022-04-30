import sqlite3

connection = sqlite3.connect('databaseRespostas.db')

with open('respostas.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO respostas (resposta) VALUES (?)",
            ('Resposta')
            )

connection.commit()
connection.close()

