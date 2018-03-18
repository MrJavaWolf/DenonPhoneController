import sys
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
translateUserInputToCommands = TranslateUserInputToCommands(commands)

#If there is no commandline arguments, we will start the mainloop and be in a "interactive mode"
if len(sys.argv) == 1:
    userInput = UserConsoleInput()
    mainLoop = MainLoop()
    mainLoop.Start(userInput, translateUserInputToCommands)

#If there are arguments we will execute the argument and return to the commandline in a non-blocking way
else:
    translateUserInputToCommands.AddInput(sys.argv[1])
    if translateUserInputToCommands.IsCommand():
        command = translateUserInputToCommands.GetCommand()
        fullUserInput = translateUserInputToCommands.GetUserInputs()
        try:
            command.Execute(fullUserInput)
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as e:
            print(traceback.format_exc())
    else:
        print("Unknown argument: '"+sys.argv[1]+"'")
denon.Close()