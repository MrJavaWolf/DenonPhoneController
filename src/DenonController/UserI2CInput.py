#http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
import smbus
import sys
import math
import time

def ReadI2CInput(bus):
    xRow = []
    yRow = []
    for i in range(3, -1, -1):
        row_to_read = int(math.pow(2, i))
        bus.write_byte(DEVICE_ADDRESS, row_to_read)
        xRow.append(bus.read_byte(DEVICE_ADDRESS))
    for i in range(4):
        row_to_read = int(math.pow(2, i + 4))
        bus.write_byte(DEVICE_ADDRESS, row_to_read)
        yRow.append(bus.read_byte(DEVICE_ADDRESS))

    inputMatrix = [[0 for y in range(4)] for x in range(4)]
    for y in range(4):
        for x in range(4):
            if xRow[x] == 0 and yRow[y] == 0:
                inputMatrix[y][x] = int(1)
    return inputMatrix

#class UserI2CInput(object):

#     def Read(self):
I2C_BUS = 1
DEVICE_ADDRESS = 0x20 #7 bit address (will be left shifted to add the read write bit)
print("Setting up the bus...")
bus = smbus.SMBus(I2C_BUS) 
while True:
    
    inputMatrix = ReadI2CInput(bus)
    print("- - - - -")
    for y in range(len(inputMatrix)):
        for x in range(len(inputMatrix[y])):
            print(str(inputMatrix[y][x]) + " ", end = '')
        print("")
    
    time.sleep(0.1)


