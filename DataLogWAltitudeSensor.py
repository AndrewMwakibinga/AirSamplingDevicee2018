#!/usr/bin/python
import os
import time 
from time import sleep
from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library

file = open("/home/pi/data_log.csv", "a")
i=0
if os.stat("/home/pi/data_log.csv").st_size == 0:
        file.write("Time,Temperature,Pressure,Sea Level\n")
while True:
        now = datetime.now()
        # Create an 'object' containing the BMP180 data
        sensor = BMP085.BMP085()
        temp = sensor.read_temperature()
        print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature()) # Temperature in Celcius
        pressure = sensor.read_pressure()
        print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()) # The local pressure
        altitude = sensor.read_altitude()
        print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude()) # The current altitude
        sea_level = sensor.read_sealevel_pressure()
        print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()) # The sea-level pressure
        file.write(str(now)+","+str(temp)+","+str(pressure)+","+str(altitude)+","+str(sea_level)+"\n")
	#have to send info to client data line by data line
        file.flush()
        time.sleep(5)
		file.close()
