#http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
import smbus

#class UserI2CInput(object):

#     def Read(self):
print("Setting up the bus...")
bus = smbus.SMBus(1) 
DEVICE_ADDRESS = 0x38      #7 bit address (will be left shifted to add the read write bit)
READ_FIRST_ROW_VALUE = 0x40

print("writes the read byte...")
#Write a single register
bus.write_byte(DEVICE_ADDRESS, READ_FIRST_ROW_VALUE)

print("reads the read byte...")
x = bus.read_byte(DEVICE_ADDRESS, READ_FIRST_ROW_VALUE)
print("Read: "+x)