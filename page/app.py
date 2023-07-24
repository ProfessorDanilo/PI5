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

def hora():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    return (year, month, day, hour, minute)



sensor = DHT.DHT11
GPIO.setmode(GPIO.BOARD)
pino_sensor = 25
umid, temp = DHT.read_retry(sensor, pino_sensor)


def salvando(umidade):
    # Crie uma conexão com o banco de dados
    conn = sqlite3.connect("dados.sql")

    # Crie um cursor
    c = conn.cursor()

    # Insira os dados na tabela
    c.execute("INSERT INTO dados (created, umidade, temperatura, pressao, CO) VALUES (?, ?, ?, ?, ?)", (hora(), umidade, 0, 0, 0))

    # Salve as alterações
    conn.commit()

    # Feche a conexão
    conn.close()

def imprimindo():
    # Crie uma conexão com o banco de dados
    conn = sqlite3.connect("meu_banco_de_dados.sqlite")

    # Crie um cursor
    c = conn.cursor()

    # Execute uma consulta SQL
    c.execute("SELECT * FROM tabela")

    # Obtenha os resultados da consulta
    rows = c.fetchall()

    # Imprima os resultados no prompt
    for row in rows:
        print(row)

    # Feche a conexão
    conn.close()


salvando(umid)
imprimindo()