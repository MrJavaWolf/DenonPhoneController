import sys
import traceback
import math
import time

class MainLoop:

    def __init__(self):
        self.HeartBeatTimeMs = 7500

    def Start(self, userInput, translateUserInputToCommands, ledController):
        isRunning = True
        while isRunning:
            self.LastHeartBeatTime = int(round(time.time() * 1000))
            sys.stdout.write("Waiting for input... [" + translateUserInputToCommands.GetUserInputs()+"]\n")
            sys.stdout.write("Input: ")
            sys.stdout.flush()
            input = self.WaitForUserInput(userInput, ledController)
            ledController.InputRead()
            sys.stdout.write(input)
            sys.stdout.write("\n")
            sys.stdout.flush()
            if input == "exit": 
                return
            translateUserInputToCommands.AddInput(input)
            if translateUserInputToCommands.IsCommand():
                command = translateUserInputToCommands.GetCommand()
                fullUserInput = translateUserInputToCommands.GetUserInputs()
                translateUserInputToCommands.Reset()
                try:
                    ledController.CommandExecuted()
                    command.Execute(fullUserInput)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except Exception as e:
                    sys.stdout.write(traceback.format_exc())
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                    
    def WaitForUserInput(self, userInput, ledController):
        userInput.PrepareForUserInput()
        containsInput = False
        input = ""
        while containsInput == False:
            time.sleep(0.05)
            input = userInput.GetUserInput()
            currentTime = int(round(time.time() * 1000))
            if currentTime - self.HeartBeatTimeMs > self.LastHeartBeatTime:
                self.LastHeartBeatTime = currentTime
                ledController.HeartBeat()
            if input != "":
                containsInput = True
        return input