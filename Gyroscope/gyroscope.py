#########References elements from http://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi ##################

import smbus

deviceAddr = 0x68   # Correct device address.

########################################
PWR_MGMT_1   = 0x6B #Need to check.
SMPLRT_DIV   = 0x19 #Need to check.
CONFIG       = 0x1A #Need to check.
GYRO_CONFIG  = 0x1B #Need to check.
INT_ENABLE   = 0x38 #Need to check.

########################################


xGyro  = 0x43 # X Axis Memory Register references.
yGyro  = 0x45 # Y Axis.
zGyro  = 0x47 # Z Axis.

def setup(devAddress, sysBus)
""" Initialise the registers for interaction """
	sysBus.write_byte_data(devAddress, SMPLRT_DIV, 7) # Determine refresh rate.
	sysBus.write_byte_data(devAddress, PWR_MGMT_1, 1) # Set power register
	sysBus.write_byte_data(devAddress, CONFIG, 0) # Set physical device config register
	sysBus.write_byte_data(devAddress, GYRO_CONFIG, 24) # Set gyroscope element register
	sysBus.write_byte_data(devAddress, INT_ENABLE, 1) # Set interrupts to be possible in the interrupt register.
	
def readData(devAddress, address, busConfig):
	#Gyro is 16 bit, join the values together using an or gate. Address is the mem registers hex ID. devAddress is the physical gyroscope.
        upperValue = busConfig.read_byte_data(devAddress, address) 
        lowerValue = busConfig.read_byte_data(devAddress, address+1)
    
        # Will join the bit values together using an OR gate I.e a 1 present in either register equals 1 as output, else = 0.
        joinUpperandLower = ((upperValue << 8) | lowerValue) # Bitwise Or statement on both registers.  << means to move bits 8 places to the left while calculating or gate value.
	 
        #Retrieves signed form of the value.
        if(joinUpperandLower > 32768): # 16bit devices have a range of -32768 to +32767 so this acts as a converter from signed to unsigned.
                joinUpperandLower = joinUpperandLower - 65536
        return joinUpperandLower

def runner(device):
	try:
            bus = smbus.SMBus(1) # Establish device connection with the serial bus.
            setup(device, bus)
            sensitivity = 131.00  #Sensitivity divisor, utilises LSB, this sets the angular velocity to 250 degrees per second(most sensitive setting).

            gyroXValue = (readData(device, xGyro, bus))/sensitivity
            gyroYValue = (readData(device, xGyro, bus))/sensitivity
            gyroZValue = (readData(device, xGyro, bus))/sensitivity
            print ("X Gyro= " + str(gyroXValue) + " Degrees per second" + " " + "Y Gyro= " + str(gyroYValue) + " Degrees per second" + " " + "Z Gyro= " + str(gyroZValue) + " Degrees per second")

        except:
            print ("Error")
	
runner(deviceAddr)


