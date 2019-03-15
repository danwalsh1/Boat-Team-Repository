#Andrew, Gareth, Adrian

import compassMain from New_compass_code.py #Compass Input
import retrieveGPS from RetrieveGPS.py #GPS Input
import gyroMain from gyroscope.py #Gyroscope Output
import RudderMain from RudderMove.py #Rudder Output
import sailMain from sail.py #Sail Output

Lat, Long = 0
startHeading = [Lat, Long]
currentHeading = startHeading
destinationHeading = []

def concatenateMain():
    print ("To stop the script press LCTRL + C")
    startInput = input("Press y to start the script")
    if startInput in ["Y", "y"]:
        boolRunning = True
        while boolRunning:
            try:
                interpretDirection(retrieveGPS(), compassMain()) #return value from retrieveGPS used as Parameter
                gyroMain()
            except KeyboardInterrupt:
                boolRunning = False
                print ("Program closing")
                exit()
                
    else:
        print ("Program closing")
        exit()

def interpretDirection(GPS, Compass):
    """Nav function that uses the GPS and compass to determine location"""
    if:
        #heading is correct
    else:
        #heading is false
        RudderMain()
        sailMain()


concatenateMain()
