import re
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
                newVolume = input[-1]
            elif re.search(regexMainZoneLong, input):
                newVolume = input[2:-1]
            print("VolumeCommand: Changes the main zone volume to: " + newVolume)
            self.denon.SetMasterVolume(newVolume)

        elif re.search(regexZone2, input):
            newVolume = input[2:-1]
            print("VolumeCommand: Changes the zone 2 volume to: " + newVolume)
            self.denon.SetZone2Volume(newVolume)

       
            
            
            
        
        return True



