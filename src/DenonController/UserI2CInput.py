#http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
import smbus
import sys
import math
import time

class UserI2CInput:

    def __init__(self, I2C_Bus_Number, I2C_Device_Address):
        self.I2C_Device_Address = I2C_Device_Address
        self.I2C_Bus_Number = I2C_Bus_Number
        self.I2C_Bus = smbus.SMBus(I2C_Bus_Number) 

    def GetUserInput(self):
        time.sleep(0.05)
        waitingForClear = True
        while waitingForClear:
            inputMatrix = self.ReadI2CInput()
            if self.IsNothingPressed(inputMatrix):
                waitingForClear = False
        
        time.sleep(0.05)
        waitingForInput = True
        while waitingForInput:
            inputMatrix = self.ReadI2CInput()
            if self.IsInputValid(inputMatrix):
                return self.InputToString(inputMatrix)

    def IsInputValid(self, inputMatrix):
        containsInput = False
        for y in range(len(inputMatrix)):
            for x in range(len(inputMatrix[y])):
                if inputMatrix[y][x] == 1:
                    #Only 1 key is allowed to be pressed at a time. If more than 1 key is pressed we will say  the input is invalid. 
                    if containsInput:
                        return False
                    else:
                        containsInput = True
        return containsInput

    def IsNothingPressed(self, inputMatrix):
        containsInput = False
        for y in range(len(inputMatrix)):
            for x in range(len(inputMatrix[y])):
                if inputMatrix[y][x] == 1: return False
        return True

    def InputToString(self, inputMatrix):
        if inputMatrix[0][0] == 1 : return "7"
        elif inputMatrix[0][1] == 1 : return "8"
        elif inputMatrix[0][2] == 1 : return "9"
        elif inputMatrix[0][3] == 1 : return "##" #C
        elif inputMatrix[1][0] == 1 : return "4"
        elif inputMatrix[1][1] == 1 : return "5"
        elif inputMatrix[1][2] == 1 : return "6"
        elif inputMatrix[1][3] == 1 : return "##" #S
        elif inputMatrix[2][0] == 1 : return "1"
        elif inputMatrix[2][1] == 1 : return "2"
        elif inputMatrix[2][2] == 1 : return "3"
        elif inputMatrix[2][3] == 1 : return "##" #D
        elif inputMatrix[3][0] == 1 : return "#" # <--
        elif inputMatrix[3][1] == 1 : return "0"
        elif inputMatrix[3][2] == 1 : return "#" # -->
        elif inputMatrix[3][3] == 1 : return "##" #I
        else: return ""

    def ReadI2CInput(self):
        xRow = []
        yRow = []
        for i in range(3, -1, -1):
            row_to_read = int(math.pow(2, i))
            self.I2C_Bus.write_byte(self.I2C_Device_Address, row_to_read)
            xRow.append(self.I2C_Bus.read_byte(self.I2C_Device_Address))
        for i in range(4):
            row_to_read = int(math.pow(2, i + 4))
            self.I2C_Bus.write_byte(self.I2C_Device_Address, row_to_read)
            yRow.append(self.I2C_Bus.read_byte(self.I2C_Device_Address))

        inputMatrix = [[0 for y in range(4)] for x in range(4)]
        for y in range(4):
            for x in range(4):
                if xRow[x] == 0 and yRow[y] == 0:
                    inputMatrix[y][x] = int(1)
        return inputMatrix


