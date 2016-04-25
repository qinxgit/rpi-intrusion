import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI 
import Adafruit_GPIO.Platform as Platform 

import time

class PIRDetector:
    initialized = False
    _gpio = None

    def __init__(self):
        initialized = False

    def Blink(self, numTimes, speed):


        for i in range(0, numTimes):
            #if i % 10 == 0:
                #print "Iteration " + str(i + 1)
            _gpio.output(7, True)
            time.sleep(speed)
            _gpio.output(7, False)
            time.sleep(speed)
        for i in range(0, numTimes):
            #if i % 10 == 0:
                #print "Iteration " + str(i + 1)
            _gpio.output(7, True)
            time.sleep(speed)
            _gpio.output(7, False)
            time.sleep(speed)

        #print 'Done'

    def Init(self):
        if not self.initialized:
            _gpio = GPIO.get_platform_gpio()
            #GPIO = Adafruit_GPIO.RPiGPIOAdapter(_gpio)
            #GPIO.setmode(GPIO.BOARD)
            
            _gpio.setup(11, GPIO.IN)
            _gpio.setup(7, GPIO.OUT)
            self.initialized = True

    def Clearup(self):
        if self.initialized:
            _gpio.cleanup()
            self.initialized = False

    def Detect(self):
        if not self.initialized:
            raise "This instance is not initialized"

        while True:
            i=_gpio.input(11)
            if i == 0:
                print "No intruders", i
                self.Blink(1, 1)
            elif i == 1:
                print "Intruder detected", i
                self.Blink(40, 0.04)

print 'OK'