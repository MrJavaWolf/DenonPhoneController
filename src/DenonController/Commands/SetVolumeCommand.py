import re
import sys

class SetVolumeCommand:

    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        regex = r"\A(22|11)?[0-9][0-9]\*"
        if re.search(regex, input) and (len(input) == 3 or len(input) == 5):
            return True
        else:
            return False

    def Execute(self, input):
        regexMainZoneShort = r"\A[0-9][0-9]\*"
        regexMainZoneLong = r"\A11[0-9][0-9]\*"
        regexZone2 = r"\A22[0-9][0-9]\*"
        if re.search(regexMainZoneShort, input) or re.search(regexMainZoneLong, input) :
            newVolume = 0
            if re.search(regexMainZoneShort, input):
                newVolume = input[0:-1]
            elif re.search(regexMainZoneLong, input):
                newVolume = input[2:-1]
            sys.stdout.write("VolumeCommand: Changes the main zone volume to: " + newVolume + "\n")
            sys.stdout.flush()
            self.denon.SetMasterVolume(newVolume)

        elif re.search(regexZone2, input):
            newVolume = input[2:-1]
            sys.stdout.write("VolumeCommand: Changes the zone 2 volume to: " + newVolume + "\n")
            sys.stdout.flush()
            self.denon.SetZone2Volume(newVolume)

       
            
            
            
        
        return True



