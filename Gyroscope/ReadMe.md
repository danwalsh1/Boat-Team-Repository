Using the smbus library. 

Read device hardware address. Presets the relevant addresses with series of register writes.

16 bit register - high and low register max range of 65536 for positional information, - 32768 to 32768. (Max possible combinations)

Formula to determine a usable signed value using 2s complement:
- in the read data function, the 16 bit register is accessed, higher and lower section, these values are merged together using an or gate. The final result is the current position of the gyroscope as a signed value between max range of 0 to 65536.

Angular velocity determined, sensitivity uses lsb to determine output. lsb set to 131.00 which is the most appropriate for the slow revolutions of the boat, higher sensitivity required for faster spinning objects.

values output in degrees per second, 250(sensitivity)/60(secs per min) = the max degrees that are recognised per second.

x is pitch, y is roll, x is yaw.
