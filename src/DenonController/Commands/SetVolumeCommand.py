import re
class SetVolumeCommand:

    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        regex = r"\A(2\*)?[0-9][0-9]\*"
        if re.search(regex, input) and (len(input) == 3 or len(input) == 5):
            return True
        else:
            return False

    def Execute(self, input):
        if not input.startswith("2*"):
            newVolume = input[:-1]
            print("VolumeCommand: Changes the main zone volume to: " + newVolume)
            self.denon.SetMasterVolume(newVolume)
        else:
            newVolume = input[2:-1]
            print("VolumeCommand: Changes the zone 2 volume to: " + newVolume)
            self.denon.SetZone2Volume(newVolume)
            
            
        
        return True


