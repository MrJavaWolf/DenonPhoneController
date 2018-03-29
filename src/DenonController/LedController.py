import RPi.GPIO as GPIO
import time

class LedController:

    def __init__(self, gpioMode, greenLed, redLed):
        self.GreenLed = greenLed
        self.RedLed = redLed
        GPIO.setmode(gpioMode)
        GPIO.setup(self.GreenLed , GPIO.OUT)
        GPIO.setup(self.RedLed , GPIO.OUT)


    def InputRead(self):
        self.OneTimeBlink(self.GreenLed, 0.3)

    def CommandExecuted(self):
        self.OneTimeBlink(self.GreenLed, 0.075)
        self.OneTimeBlink(self.GreenLed, 0.075)
        self.OneTimeBlink(self.GreenLed, 0.075)

    def HeartBeat(self):
        self.OneTimeBlink(self.GreenLed, 0.05)

    def Error(self):
        self.OneTimeBlink(self.RedLed, 0.5)

    def OneTimeBlink(self, led, sleepTime):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(led, GPIO.LOW)
        time.sleep(sleepTime)
