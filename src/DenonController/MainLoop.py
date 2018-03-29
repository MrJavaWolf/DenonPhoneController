import sys
import traceback

class MainLoop:

    def Start(self, userInput, translateUserInputToCommands, ledController):
        isRunning = True
        while isRunning:
            sys.stdout.write("Waiting for input... [" + translateUserInputToCommands.GetUserInputs()+"]\n")
            sys.stdout.write("Input: ")
            sys.stdout.flush()
            input = userInput.GetUserInput()
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
                    
