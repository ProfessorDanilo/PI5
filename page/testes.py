import datetime
import sqlite3
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
print(minute)



# Crie uma conexão com o banco de dados
conn = sqlite3.connect("dados.db")

# Crie um cursor
c = conn.cursor()

# Execute uma consulta SQL
c.execute("SELECT * FROM dados")

# Obtenha os resultados da consulta
rows = c.fetchall()

# Imprima os resultados no prompt
print("ano\tmes\tdia\thora\tminuto\tumid\ttemp\tpressao monoxido de carbono")
for row in rows:
    for i in range(9):
        print(row[i], end="\t")
    print()


# Feche a conexão
conn.close()





""" 
connection = sqlite3.connect('aulas_resultados.db')

with open('aulas_resultados.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("SELECT * FROM ranking ORDER BY pontuacao DESC;")

rows = cur.fetchall()

for row in rows:
    print(row[2])
    print(row[3])


connection.commit()
connection.close() """
