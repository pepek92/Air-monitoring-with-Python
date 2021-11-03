import time 
from time import sleep
from datetime import datetime
import sys
import adafruit_dht
import board
import sqlite3


dhtDevice = adafruit_dht.DHT22(board.D4,use_pulseio=False)
conn = sqlite3.connect('temperature.db')
cur = conn.cursor()

while True:
	try:
		temperature = dhtDevice.temperature
		humidity = dhtDevice.humidity
		now = datetime.now()
		date=now.strftime("%Y/%m/%d")
		time=now.strftime("%H:%M")
		cur.execute("INSERT INTO dhsensor(Temperature, Humidity, Date, Time) VALUES(?,?,?,?)", (temperature, humidity, date, time))
		conn.commit()
		sleep(300.0)

	except RuntimeError as error:
		sleep(60.0)
		continue
	except Exception as error:
		dhtDevice.exit()
		raise error

