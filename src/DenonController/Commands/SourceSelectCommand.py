import re
class SourceSelectCommand(object):
    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        regex = r"\A(11[0-9]|21[0-9]|300|301)"
        if re.search(regex, input) and len(input) == 3:
            return True
        else:
            return False

    def Execute(self, input):
        if input == "110":
            print("SourceSelectCommand: Selects input source PC (SAT/CBL)")
            self.denon.SelectSourceSATCBL()
        elif input == "111":
            print("SourceSelectCommand: Selects input source ChromeCast (DVD)")
            self.denon.SelectSourceDVD()
        elif input == "112":
            print("SourceSelectCommand: Selects input source InternetRadio")
            self.denon.SelectSourceInternetRadio()
        elif input == "113":
            print("SourceSelectCommand: Selects input source Lion Bluetooth (CD)")
            self.denon.SelectSourceCD()
        elif input == "210":
            print("SourceSelectCommand: Selects input source zone 2 InternetRadio")
            self.denon.Zone2_SelectSourceInternetRadio()
        elif input == "211":
            print("SourceSelectCommand: Selects input source zone 2 Lion Bluetooth (CD)")
            self.denon.Zone2_SelectSourceCD()
        elif input == "300":
            print("SourceSelectCommand: Selects input source zone 2 - same as Main zone")
            self.denon.Zone2_SelectSourceSyncWithMainZone()
        elif input == "301":
            print("SourceSelectCommand: Selects input source zone 2 and Main zone is no longer the same")
            self.denon.Zone2_SelectSourceUnsyncWithMainZone()
