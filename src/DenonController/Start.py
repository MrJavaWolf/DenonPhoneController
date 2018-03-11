import DenonCommands
from MainLoop import MainLoop
from UserConsoleInput import UserConsoleInput
from DenonConnection import DenonConnection 
from TranslateUserInputToCommands import TranslateUserInputToCommands 
from Commands import *

#Connection
Denon_IP = '192.168.0.12'
Denon_Port = 23 #Default port 23 (Telnet)

def GetCommands(denon):
    return [ResetInputsCommand.ResetInputsCommand(),
            SetVolumeCommand.SetVolumeCommand(denon),
            PowerCommand.PowerCommand(denon),
            MuteCommand.MuteCommand(denon),
            SourceSelectCommand.SourceSelectCommand(denon),
            ListenCommand.ListenCommand(denon)]

print("Welcome to JWolf's Denon controls!")
denon = DenonConnection(Denon_IP, Denon_Port)
commands = GetCommands(denon)
userInputToCommands = TranslateUserInputToCommands(commands)
userInput = UserConsoleInput()
mainLoop = MainLoop()
mainLoop.Start(userInput, userInputToCommands)

denon.Close()