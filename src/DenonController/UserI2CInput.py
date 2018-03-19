#http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
import smbus
import sys
import math

#class UserI2CInput(object):

#     def Read(self):
I2C_BUS = 1
DEVICE_ADDRESS = 0x20 #7 bit address (will be left shifted to add the read write bit)
w, h = 4, 4
print("Setting up the bus...")
bus = smbus.SMBus(I2C_BUS_NUMBER) 
Matrix = [[0 for x in range(w)] for y in range(h)]
result_x[4]
result_y[4]
for i in range(4):
    row_to_read = math.pow(2, i)
    bus.write_byte(DEVICE_ADDRESS, row_to_read)
    result_x[i] = bus.read_byte(DEVICE_ADDRESS)
for i in range(4):
    row_to_read = math.pow(2, i + 4)
    bus.write_byte(DEVICE_ADDRESS, row_to_read)
    result_y[i] = bus.read_byte(DEVICE_ADDRESS)

print("xvalues: " + ", ".join(result_x))
print("yvalues: " + ", ".join(result_y))

