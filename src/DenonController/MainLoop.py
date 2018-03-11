import sys
import traceback

class MainLoop:

    def Start(self, userInput, translateUserInputToCommands):
        isRunning = True
        while isRunning:
            print("Please enter your input: " + translateUserInputToCommands.GetUserInputs(), end='')
            input = userInput.GetUserInput()
            if input == "exit": 
                return
            translateUserInputToCommands.AddInput(input)
            if translateUserInputToCommands.IsCommand():
                command = translateUserInputToCommands.GetCommand()
                fullUserInput = translateUserInputToCommands.GetUserInputs()
                translateUserInputToCommands.Reset()
                try:
                    command.Execute(fullUserInput)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except Exception as e:
                    print(traceback.format_exc())
                    
