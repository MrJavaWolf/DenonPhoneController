class PowerCommand:

    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        if input == "000" or input == "100" or input == "101" or input == "200" or input == "201":
            return True
        else:
            return False

    def Execute(self, input):
        if input == "000":
            print("PowerCommand: Turns off the all zones")
            self.denon.Zone2PowerOff()
            self.denon.PowerOff()
        elif input == "100":
            print("PowerCommand: Turns on the main zone")
            self.denon.PowerOn()
        elif input == "101":
            print("PowerCommand: Turns off the main zone")
            self.denon.PowerOff()
        elif input == "200":
            print("PowerCommand: Turns on the zone2")
            self.denon.Zone2PowerOn()
        elif input == "201":
            print("PowerCommand: Turns off the zone2")
            self.denon.Zone2PowerOff()
