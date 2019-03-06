#########References elements from http://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi ##################

import smbus

deviceAddr = 0x68   # Correct device address.
PWR_MGMT_1   = 0x6B #Need to check.
SMPLRT_DIV   = 0x19 #Need to check.
CONFIG       = 0x1A #Need to check.
GYRO_CONFIG  = 0x1B #Need to check.
INT_ENABLE   = 0x38 #Need to check.
xGyro  = 0x43 # X Axis Memory Register references.
yGyro  = 0x45 # Y Axis - Need to check.
zGyro  = 0x47 # Z Axis - Need to check.

def setup(devAddress, bus):
	bus.write_byte_data(devAddress, SMPLRT_DIV, 7) # Set sample register
	bus.write_byte_data(devAddress, PWR_MGMT_1, 1) # Set power register
	bus.write_byte_data(devAddress, CONFIG, 0) # Set physical device config register
	bus.write_byte_data(devAddress, GYRO_CONFIG, 24) # Set gyroscope element register
	bus.write_byte_data(devAddress, INT_ENABLE, 1) # Set interrupts to be possible in the interrupt register.
	
def readData(devAddress, address, busConfig):
	#Gyro is 16 bit, 2 bytes of information, one value will be used, the other dropped based on value presence<Or gate principals>.
        upperValue = busConfig.read_byte_data(devAddress, address) 
        lowerValue = busConfig.read_byte_data(devAddress, address+1)
    
        # Will join the values together used OR gate principal, if present in either = 1, else = 0.
        joinUpperandLower = ((upperValue << 8) | lowerValue) # Bitwise Or statement, << means to move bits 8 places to the left(Clears the register byte).
        
        #Retrieves signed form of the value.
        if(joinUpperandLower > 32768): # 16bit devices have a range of -32768 to +32767 so this acts as a Analog to Digital converter.
                joinUpperandLower = joinUpperandLower - 65536
        return joinUpperandLower

def runner(device):
	
	bus = smbus.SMBus(1) # Establish device connection with the serial bus.
	setup(device, bus)
	sensitivity = 131.00  #Sensitivity divisor, utilises LSB, is the most accurate/sensitive the gyroscope module can be.
	
	gyroXValue = (readData(device, xGyro, bus))/sensitivity
	gyroYValue = (readData(device, xGyro, bus))/sensitivity
	gyroZValue = (readData(device, xGyro, bus))/sensitivity 
	

	print ("X Gyro= " + str(gyroXValue) + " Degrees per second" + " " + "Y Gyro= " + str(gyroYValue) + " Degrees per second" + " " + "Z Gyro= " + str(gyroZValue) + " Degrees per second")

runner(deviceAddr)

