#!/usr/bin/env python
import LCD1602
import time
import os

ds18b20 = '' 

def setup():
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.write(0, 0, 'Greetings!!')
	LCD1602.write(1, 1, 'Booting up!')
	global ds18b20
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master1':
			ds18b20 = i
	time.sleep(2)
	read()

def loop():
	space = '                '
	greetings = 'Thank you for buying SunFounder Sensor Kit for Raspberry! ^_^'
	greetings = space + greetings
	while True:
		tmp = greetings
		for i in range(0, len(greetings)):
			LCD1602.write(0, 0, tmp)
			tmp = tmp[1:]
			time.sleep(0.02)
			#LCD1602.clear()
def myLoop():
	LCD1602.clear()
	while True:
		if read() != None:
			temp = read()
			cTemp = 'Temp: ' + str(temp) + ' C'
			LCD1602.write(0,0, cTemp )
			fTemp = 'Temp: ' + str((temp*1.8)+32)+ ' F' 
			LCD1602.write(1,1, fTemp)
			time.sleep(600)

def read():
#	global ds18b20
	print"making Read"
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	tfile = open(location)
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	return temperature

def destroy():
	pass	

if __name__ == "__main__":
	try:
		setup()
		while True:
			time.sleep(2)
			myLoop()
	except KeyboardInterrupt:
		destroy()
