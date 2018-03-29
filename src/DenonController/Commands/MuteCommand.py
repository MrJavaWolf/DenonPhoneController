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
            print("MuteCommand: Toggles main zone mute")
            if self.denon.IsMuted():
                print("MuteCommand: Main zone mute off")
                self.denon.MuteOff()
            else:
                print("MuteCommand: Main zone mute on")
                self.denon.MuteOn()
        elif input == "205*":
            print("MuteCommand: Toggles zone2 mute")
            if self.denon.Zone2IsMuted():
                print("MuteCommand: Main zone mute off")
                self.denon.Zone2MuteOff()
            else:
                print("MuteCommand: Main zone mute on")
                self.denon.Zone2MuteOn()
            
