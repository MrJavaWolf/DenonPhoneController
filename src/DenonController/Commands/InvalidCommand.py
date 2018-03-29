class InvalidCommand:
    def __init__(self, ledController):
        self.ledController = ledController

    def CanExecute(self, input):
        if input == "*" or input.endswith("*"):
            return True
        else:
            return False

    def Execute(self, input):
        print("Invalid command")
        ledController.InvalidCommand()


