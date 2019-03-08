#Adrian and Hannia

#Reference: Gareth's GPS retrieve pseudocode

import serial      #Import serial to define the path of gyroscope.
import pynmea2     #Installation of pynmea2 library.



def retrieveGPS();
	device = "/dev/<devId>" 		#This will be the path to the device on the Pi.
	TRY:
		gpsSerialSetup = serial.Serial(device, baudrate= 9600, timeout=1)
		gpsDataRead = gpsSerialSetup.readline()
		if gpsDataRead == '$deviceLongAndLatOutTag’:  
			getLongAndLatData = pynmea2.parse(readData)
			print(getLongAndLatData.lattitude + " " + getLongAndLatData.longitude)
			return("Success")
	EXCEPT:
		print("GPS can not be read")
		return("Failed")