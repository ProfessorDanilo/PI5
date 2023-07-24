from pickle import FALSE
from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3
from time import sleep
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort
import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
import time

now = datetime.datetime.now()
ano = now.year
mes = now.month
dia = now.day
hora = now.hour
minuto = now.minute



sensor = DHT.DHT11
GPIO.setmode(GPIO.BOARD)
pino_sensor = 25
umid, temp = DHT.read_retry(sensor, pino_sensor)


# Crie uma conexão com o banco de dados
conn = sqlite3.connect("dados.db")

# Crie um cursor
c = conn.cursor()

# Insira os dados na tabela
c.execute("INSERT INTO dados (ano, mes, dia, hora, minuto, umidade, temperatura, pressao, CO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (ano, mes, dia, hora, minuto, umid, temp, 0, 0))

# Salve as alterações
conn.commit()

# Feche a conexão
conn.close()

# Crie uma conexão com o banco de dados
conn = sqlite3.connect("dados.db")

# Crie um cursor
c = conn.cursor()

# Execute uma consulta SQL
c.execute("SELECT * FROM dados")

# Obtenha os resultados da consulta
rows = c.fetchall()

# Imprima os resultados no prompt
for row in rows:
    print(row)

# Feche a conexão
conn.close()

