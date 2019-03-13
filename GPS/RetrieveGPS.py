#Adrian and Hannia

#Reference: Gareth's GPS retrieve pseudocode
#Debugged by Dan

import serial      #Import serial to define the path of gyroscope.
import pynmea2     #Installation of pynmea2 library.

def retrieveGPS();
	device = "/dev/ttyS0" 		#This will be the path to the device on the Pi.
	try:
		gpsSerialSetup = serial.Serial(device, baudrate= 9600, timeout=1)
		gpsDataRead = gpsSerialSetup.readline()
		gpsDataReadArr = gpsDataRead.split(",")
		if gpsDataReadArr[0] == "$GPRMC":  
			getLongAndLatData = pynmea2.parse(readData)
			return([getLongAndLatData.lat,getLongAndLatData.lon])
	except Exception as e:
		print("GPS can not be read")
		return("Failed")
print(retrieveGPS())
