import RPi.GPIO as GPIO
import time
import threading

class LedController:

    def __init__(self, gpioMode, greenLed, redLed):
        self.GreenLed = greenLed
        self.RedLed = redLed
        GPIO.setmode(gpioMode)
        GPIO.setwarnings(False)
        GPIO.setup(self.GreenLed , GPIO.OUT)
        GPIO.setup(self.RedLed , GPIO.OUT)
        self.stopWorkerThread = False;
        self.Execute = None
        self.ExecuteCounter = 0
        workerThread = threading.Thread(target=self.StartWorkerTread)
        workerThread.start()

    def StartWorkerTread(self):
        while self.stopWorkerThread == False:
            time.sleep(0.02)
            while self.Execute is not None and self.stopWorkerThread == False:
                currentExecuteCounter = self.ExecuteCounter
                self.Execute()
                if self.ExecuteCounter == currentExecuteCounter:
                    self.Execute = None
    
    def UpdateExecuteCounter(self):
        self.ExecuteCounter = self.ExecuteCounter + 1 

    def Close():
        self.stopWorkerThread = True

    def InputRead(self):
        self.Execute = self.InputReadBlocking
        self.UpdateExecuteCounter()

    def InputReadBlocking(self):
        self.OneTimeBlink(self.GreenLed, 0.3)
    
    def CommandExecuted(self):
        self.Execute = self.CommandExecutedBlocking
        self.UpdateExecuteCounter()

    def CommandExecutedBlocking(self):
        self.OneTimeBlink(self.GreenLed, 0.075)
        time.sleep(0.075)
        self.OneTimeBlink(self.GreenLed, 0.075)
        time.sleep(0.075)
        self.OneTimeBlink(self.GreenLed, 0.075)

    def HeartBeat(self):
        self.Execute = self.HeartBeatBlocking
        self.UpdateExecuteCounter()

    def HeartBeatBlocking(self):
        self.OneTimeBlink(self.GreenLed, 0.05)

    def Error(self):
        self.Execute = self.ErrorBlocking
        self.UpdateExecuteCounter()

    def ErrorBlocking(self):
        self.OneTimeBlink(self.RedLed, 0.5)

    def OneTimeBlink(self, led, sleepTime):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(led, GPIO.LOW)