from flask import Flask, render_template, url_for, jsonify, request
from datetime import datetime
import sys
import json
import sqlite3
import random

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('temperature.db')
    conn.row_factory = sqlite3.Row
    return conn

def load_temp():
    conn = get_db_connection()
    result = conn.execute("SELECT Temperature FROM dhsensor ORDER BY id DESC limit 10;").fetchall()
    conn.close()
    return list(result)

def load_hum():
    conn = get_db_connection()
    result = conn.execute("SELECT Humidity FROM dhsensor ORDER BY id DESC limit 10;").fetchall()
    conn.close()
    return list(result)

def load_date():
    conn = get_db_connection()
    result = conn.execute("SELECT Date FROM dhsensor ORDER BY id DESC limit 10;").fetchall()
    conn.close()
    return list(result)

def load_time():
    conn = get_db_connection()
    result = conn.execute("SELECT Time FROM dhsensor ORDER BY id DESC limit 10;").fetchall()
    conn.close()
    return list(result)

@app.route('/')
def index():
    temp = load_temp()
    hum = load_hum()
    date = load_date()
    time = load_time()
    return render_template("index.html", temp = temp, hum = hum, date = date, time = time)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)