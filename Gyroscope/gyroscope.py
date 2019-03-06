#########References elements from http://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi ##################

import smbus

deviceAddr = 0x68   # Identify this address, needs to be changed, can use I2Cdetect on the Pi.
PWR_MGMT_1   = 0x6B #Need to check.
SMPLRT_DIV   = 0x19 #Need to check.
CONFIG       = 0x1A #Need to check.
GYRO_CONFIG  = 0x1B #Need to check.
INT_ENABLE   = 0x38 #Need to check.
xGyro  = 0x43 # X Axis Memory Register references.
yGyro  = 0x45 # Y Axis - Need to check.
zGyro  = 0x47 # Z Axis - Need to check.

def setup(devAddress):

bus.write_byte_data(devAddress, SMPLRT_DIV, 7) # Set sample register
	bus.write_byte_data(devAddress, PWR_MGMT_1, 1) # Set power register
	bus.write_byte_data(devAddress, CONFIG, 0) # Set physical device config register
	bus.write_byte_data(devAddress, GYRO_CONFIG, 24) # Set gyroscope element register
	bus.write_byte_data(devAddress, INT_ENABLE, 1) # Set interrupts to be possible in the interrupt register.
	
def readData(devAddress, address, busConfig):
	#Accelero and Gyro value are 16-bit
        high = busConfig.read_byte_data(devAddress, address) 
        low = busConfig.read_byte_data(devAddress, address+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low) # Bitwise Or statement, << means to move bits 8 places to the left(Clears the register byte).
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

def runner(device):
	
	setup(device)
	bus = smbus.SMBus(1) # Establish device connection with the serial bus.
	
	sensitivity = 131.00  #Sensitivity divisor, uses LSB, is the most accurate the gyroscope module can be.
	readGyroX = readData(device, xGyro, bus)
	readGyroY = readData(device, yGyro, bus)
	readGyroZ = readData(device, zGyro, bus)
	
	gyroXValue = readGyroX/sensitivity
	gyroYValue = readGyroY/sensitivity
	gyroZValue = readGyroZ/sensitivity 
	

	print ("X Gyro= " + str(gyroXValue) + " Degrees per second", "Y Gyro= " + str(gyroYValue) + " Degrees per second, "Z Gyro= " + str(gyroZValue) + " Degrees per second")

runner(deviceAddr)

