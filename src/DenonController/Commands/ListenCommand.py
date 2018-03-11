
class ListenCommand:
    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        if input == "999":
            return True
        else:
            return False

    def Execute(self, input):
        print("ListenCommand: Will listen forever...")
        while True:
            responseBytes = self.denon.WaitForResponse(["\r"])
            response = responseBytes.decode("ascii")
            print(response)
