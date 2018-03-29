import sys
import DenonCommands
from MainLoop import MainLoop
from UserConsoleInput import UserConsoleInput
from UserI2CInput import UserI2CInput
from LedController import LedController 
from DenonConnection import DenonConnection 
import RPi.GPIO as GPIO
from TranslateUserInputToCommands import TranslateUserInputToCommands 
from Commands import *
import ptvsd

ptvsd.enable_attach(secret='debug')

#Denon Connection
Denon_IP = '192.168.0.12'
Denon_Port = 23 #Default port 23 (Telnet)

#IC2
I2C_Bus_Number = 1
I2C_Device_Address = 0x20

#Leds
Gpio_Mode = GPIO.BOARD
Led_Green = 16
Led_Red = 12

def GetCommands(denon, ledController):
    return [ResetInputsCommand.ResetInputsCommand(),
            #ListenCommand.ListenCommand(denon),
            SetVolumeCommand.SetVolumeCommand(denon),
            PowerCommand.PowerCommand(denon),
            MuteCommand.MuteCommand(denon),
            SourceSelectCommand.SourceSelectCommand(denon),
            InvalidCommand.InvalidCommand(ledController)]

print("Welcome to JWolf's Denon controls!")
denon = DenonConnection(Denon_IP, Denon_Port)
ledController = LedController(Gpio_Mode, Led_Green, Led_Red)

commands = GetCommands(denon, ledController)
translateUserInputToCommands = TranslateUserInputToCommands(commands)

try:
    #If there is no commandline arguments, we will start the mainloop and be in
    #an "interactive mode"
    if len(sys.argv) == 1:
        userI2CInput = UserI2CInput(I2C_Bus_Number, I2C_Device_Address, ledController)
        mainLoop = MainLoop()
        mainLoop.Start(userI2CInput, translateUserInputToCommands, ledController)


    #If there are arguments we will execute the argument and return to the
    #commandline in a non-blocking way
    else:
        translateUserInputToCommands.AddInput(sys.argv[1])
        if translateUserInputToCommands.IsCommand():
            command = translateUserInputToCommands.GetCommand()
            fullUserInput = translateUserInputToCommands.GetUserInputs()
            try:
                ledController.CommandExecuted()
                command.Execute(fullUserInput)
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception as e:
                print(traceback.format_exc())
        else:
            print("Unknown argument: '" + sys.argv[1] + "'")

finally:
    denon.Close()
    ledController.Close()