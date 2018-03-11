class TranslateUserInputToCommands:
    
    def __init__(self, commands):
        self.commands = commands
        self.userInputs = ""

    def GetUserInputs(self):
        return self.userInputs

    def AddInput(self, input):
        self.userInputs+= input
    
    def IsCommand(self):
        for command in self.commands:
            if command.CanExecute(self.userInputs):
                return True
        return False

    def Reset(self):
        self.userInputs = ""

    def GetCommand(self):
        for command in self.commands:
            if command.CanExecute(self.userInputs):
                return command
        return False
