
class ListenCommand:
    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        if input == "999*":
            return True
        else:
            return False

    def Execute(self, input):
        sys.stdout.write("ListenCommand: Will listen forever...\n")
        sys.stdout.flush()

        while True:
            responseBytes = self.denon.WaitForResponse(["\r"])
            response = responseBytes.decode("ascii")
            sys.stdout.write(response)
            sys.stdout.write("\n")
            sys.stdout.flush()
