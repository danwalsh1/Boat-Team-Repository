Andrew/Hardeep
#this part of the code was copied in part from gareth and adrians work 

import RPi.GPIO as GPIO

#straight -> 0Hz
#starboard, hard -> 90Hz
#port, hard -> -90Hz
pi = 3.14159265359

def setupPi(frequency):
    GPIO.setmode(GPIO.BOARD) #uses board pins
    GPIO.setup(12, GPIO.OUT) #sets pin 18 as the output (rudder motor)
    pinsetup = GPIO.PWM(12,frequency)#rudder is set to straight
    pin.start(1) #sets initial position of rudder
    return pinsetup

def runPi(pin):
    try:
        print("Attempting to set rudder servo")
        GPIO.output(12,1) #sends a HIGH signal to pin 12
    except:
        print("Error")
        return "Failed"

    finally:
        pin.stop()
        GPIO.cleanup() #Clean up after yourself
    return "Success"

def main():
    DegAngle = float(input())
    while (DegAngle > -90 and DegAngle < 90):
        RadAngle = DegAngle * (pi/180) 
        
    setup = setupPi(RadAngle)
    runPi(setup)
