class ResetInputsCommand:

    def CanExecute(self, input):
        if input == "#" or input.endswith("##"):
            return True
        else:
            return False

    def Execute(self, input):
        return True


