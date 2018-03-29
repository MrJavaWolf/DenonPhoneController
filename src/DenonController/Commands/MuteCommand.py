class MuteCommand(object):

    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        if input == "105*" or input == "205*":
            return True
        else:
            return False

    def Execute(self, input):
        if input == "105*":
            sys.stdout.write("MuteCommand: Toggles main zone mute\n")
            sys.stdout.flush()
            if self.denon.IsMuted():
                sys.stdout.write("MuteCommand: Main zone mute off\n")
                sys.stdout.flush()
                self.denon.MuteOff()
            else:
                sys.stdout.write("MuteCommand: Main zone mute on\n")
                sys.stdout.flush()
                self.denon.MuteOn()
        elif input == "205*":
            sys.stdout.write("MuteCommand: Toggles zone2 mute\n")
            sys.stdout.flush()
            if self.denon.Zone2IsMuted():
                sys.stdout.write("MuteCommand: Main zone mute off\n")
                sys.stdout.flush()
                self.denon.Zone2MuteOff()
            else:
                sys.stdout.write("MuteCommand: Main zone mute on\n")
                sys.stdout.flush()
                self.denon.Zone2MuteOn()
            
