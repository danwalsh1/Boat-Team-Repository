#Hardeep 
#Reset rudder and sail to starting position
#Refrence for sail code: part copied from Gareth and Adrians work  

import Rpi.GPIO as GPIO

#Rudder setupPi

def setupPi(frequency):
    GPIO.setmode(GPIO.BOARD) #uses board pins
    GPIO.setup(12, GPIO.OUT) #sets pin 18 as the output (rudder motor)
    pinsetup = GPIO.PWM(12,frequency)#rudder is set to straight
    pin.start(1) #sets initial position of rudder
    return pinsetup

#Sail setupPi 

def setupPi():

    GPIO.setmode(GPIO.BOARD)  # define use of Board mode.
    GPIO.setup(11, GPIO.OUT)  # Set pin 11(gpio 17) to be an output.
    pinsetup = GPIO.PWM(11, 50)  # Pin and frequency of PWM.
    return pinsetup

#rudder reset 

def setRudder(pin, angle):
    
    dutyChange = int(angle/18) + 1 

    try:
          print("Attempting to reset rudder servo")
          pin.start(1)
          pin.ChangeDutyCycle(dutyChange)
          time.sleep(5) #until change has been made. 
    except:
        print("error,, servo contact has been interrupted")
        return "Failed"
    finally:
        pin.stop()
        GPIO.cleanup()

    return "Success"

setup = setupPi()
#runner =true

rudderAngle = int(90) #this should set rudder to 90 degrees starting point 

while runner :
    rudderAngle = int(90) #this should set rudder to 90 degrees starting point
    
if rudderAngle == "q" or rudderAngle == "Q":
    runner = false
    print("finished")

setrudder(setup, rudderAngle) 

#Sail reset    

def setSail(pin, angle):
    
    dutyChange = int(angle/18) + 1

    try:
        print("Attempting to reset sail servo")
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


setup = setupPi() 
#runner = true

sailAngle = int(90)  #this should set sail to 90 degrees starting point 


while runner:
    sailAngle = int(90)  #this should set sail to 90 degrees starting point 
    if sailAngle == "q" or sailAngle == "Q":
        runner = false
        print("Finished")
 
setSail(setup, sailAngle)







