import datetime
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
print(minute)


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
