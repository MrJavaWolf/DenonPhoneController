class UserConsoleInput:

    def GetUserInput(self):
        userInput = ""
        while not self.IsValidUserInput(userInput):
            userInput = input()
            if not self.IsValidUserInput(userInput):
                self.ShowValidInputsToUser()
        return userInput

    def ShowValidInputsToUser(self):
        print("Please provide an valid input. Valid inputs are: 0-9, * and #")

    def IsValidUserInput(self, userInput):
        if not userInput:
           return False
        if len(userInput) == 0: 
            return False
        if userInput == "":
            return False
        if userInput == "exit":
            return True
        for c in userInput:
            if not self.IsValidUserInputCharacter(c):
                return False
        return True

    def IsValidUserInputCharacter(self, userInput):
        if userInput.isdigit() or userInput == "#" or userInput == "*": 
            return True
        return False



