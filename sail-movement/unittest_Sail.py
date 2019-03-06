#Adrian and Gareth

import unittest
import RPi.GPIO as GPIO
from mock import Mock, patch

class TestSail(unittest.TestCase):
  
  def test_setup(self):
    rpi_gpio = Mock()
    GPIO = GPIO_TestSail(rpi_gpio)
    GPIO.start(11, 50)
    rpi_gpio.GPIO.assert_called_with(1, 2000)
  
  def test_set_duty_cycle_valid(self):
    rpi_gpio = Mock()
    GPIO = GPIO.TestSail(rpi_gpio)
    GPIO.start(11, 50)           #pin and frequency of PWM
    GPIO.set_duty_cycle(11, 7.5) #7 middle, 2 start, 12 to 14 end
    
  def test_set_duty_cycle_invalid(self):
    rpi_gpio = Mock()
    GPIO = GPIO.TestSail(rpi_gpio)
    GPIO.start(11, 7.5)
    self.assertRaises(ValueError, GPIO.set_duty_cycle, 11, 15)
    self.assertRaises(ValueError, GPIO.set_duty_cycle, 11, -1)
    
  def test_set_frequency(self):
    rpi_gpio = Mock()
    GPIO = GPIO.TestSail(rpi_gpio)
    GPIO.start(1, 50)
    GPIO.set_frequency(1, 1000)
    
    
if __name__ == '__main__':
  unittest.main()