#Hardeep and Andrew
#This part of the code was copied in part from gareth and adrians work
import RPi.GPIO as GPIO

def setupPi(frequency):
    GPIO.setmode(GPIO.BOARD) #uses board pins
    GPIO.setup(12, GPIO.OUT) #sets pin 18 as the output (rudder motor)
    pinsetup = GPIO.PWM(12,frequency)#rudder is set to straight
    pin.start(1) #sets initial position of rudder
    return pinsetup

def setRudder(pin, angle):
    
    dutyChange = int(angle/18) + 1 

    try:
          print("Attempting to set rudder servo")
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

def RudderMain():
    setup = setupPi()
    #runner =true

    rudderAngle = int(input("enter the angle you would like teh rudder then press enter: "))

    while runner :
        rudderAngle = int(input("enter teh angle you would like the rudder then press enter: "))

    if rudderAngle == "q" or rudderAngle == "Q":
        runner = false
        print("finished")

    setrudder(setup, rudderAngle) 
