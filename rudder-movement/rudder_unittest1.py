#Hardeep and Andrew 
#This work is part Similar to the work of Adrian and Gareths sail code 

import unittest
import RPi.GPIO as GPIO
from mock import mock, patch 

class TestRudderDirection(unittest.TestCase):
    
    def test_setupPi(self):
        rpi_gpio = Mock()
        GPIO = GPIO_TestRudderDirection(rpi_gpio)
        GPIO.start(12,18)
        rpi_gpio.GPIO.assert_called_with(1, 1000)

    def test_set_duty_cycle_valid(self):
        rpi_gpio = Mock()
        GPIO = GPIO.TestRudderDirection(rpi_gpio)
        GPIO.start(12, 50)           #pin and frequency of PWM
        GPIO.set_duty_cycle(12, 7.5) 
    
    def test_set_duty_cycle_invalid(self):
        rpi_gpio = Mock()
        GPIO = GPIO.TestRudderDirection(rpi_gpio)
        GPIO.start(12, 7.5)
        self.assertRaises(ValueError, GPIO.set_duty_cycle, 12, 15)
        self.assertRaises(ValueError, GPIO.set_duty_cycle, 12, -1)
    
    def test_set_frequency(self):
        rpi_gpio = Mock()
        GPIO = GPIO.TestRudderDirection(rpi_gpio)
        GPIO.start(12, 50)
        GPIO.set_frequency(1, 800)


if __name__ == '__main__':
    unittest.main()
