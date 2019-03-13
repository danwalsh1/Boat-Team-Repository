#Adrian and Gareth
#Please reference the file if you use this code.

import RPi.GPIO as GPIO
import time

def setupPi():

    GPIO.setmode(GPIO.BOARD)  # define use of Board mode.
    GPIO.setup(11, GPIO.OUT)  # Set pin 11(gpio 17) to be an output.
    pinsetup = GPIO.PWM(11, 50)  # Pin and frequency of PWM.
    return pinsetup

def setSail(pin, angle):
    
    dutyChange = int(angle/18) + 1

    try:
        print("Attempting to set sail servo")
        pin.start(0)  # Sets the initial position.
        pin.ChangeDutyCycle(dutyChange) # 7 is the middle point for the servo, 1 is the start, 12 to 14 is the end.
        time.sleep(5) # Sleep until change is made.
    except:
        print("Error, servo contact has been interrupted")
        return "Failed"
    finally:
        pin.stop() # Stops the pin running high.
        GPIO.cleanup() # Resets pins to default starting state.
    
    return "Success"

def sailMain():
    setup = setupPi() 
    #runner = true

    sailAngle = int(input("Please enter the angle you would like the sail and then press enter: ")) #90 degrees as the angle is central starting location.

    """
    while runner:
        sailAngle = int(input("Please enter the angle you would like the sail and then press enter: ")) # 90 degrees as the angle is currently central starting location.
        if sailAngle == "q" or sailAngle == "Q":
            runner = false
            print("Finished")
    """    
    setSail(setup, sailAngle)
