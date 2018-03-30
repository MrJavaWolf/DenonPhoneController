import re
import sys

class SourceSelectCommand(object):
    def __init__(self, denon):
        self.denon = denon

    def CanExecute(self, input):
        regex = r"\A(11[0-9]\*|21[0-9]\*|300\*|301\*)"
        if re.search(regex, input) and len(input) == 4:
            return True
        else:
            return False

    def Execute(self, input):
        if input == "110*":
            sys.stdout.write("SourceSelectCommand: Selects input source PC (SAT/CBL)\n")
            sys.stdout.flush()
            self.denon.SelectSourceSATCBL()
        elif input == "111*":
            sys.stdout.write("SourceSelectCommand: Selects input source ChromeCast (DVD)\n")
            sys.stdout.flush()
            self.denon.SelectSourceDVD()
        elif input == "112*":
            sys.stdout.write("SourceSelectCommand: Selects input source Internet Radio\n")
            sys.stdout.flush()
            self.denon.SelectSourceInternetRadio()
        elif input == "113*":
            sys.stdout.write("SourceSelectCommand: Selects input source Lion Bluetooth (CD)\n")
            sys.stdout.flush()
            self.denon.SelectSourceCD()
        elif input == "210*":
            sys.stdout.write("SourceSelectCommand: Selects input source zone 2 InternetRadio\n")
            sys.stdout.flush()
            self.denon.Zone2_SelectSourceInternetRadio()
        elif input == "211*":
            sys.stdout.write("SourceSelectCommand: Selects input source zone 2 Lion Bluetooth (CD)\n")
            sys.stdout.flush()
            self.denon.Zone2_SelectSourceCD()
        elif input == "300*":
            sys.stdout.write("SourceSelectCommand: Selects input source zone 2 - same as Main zone\n")
            sys.stdout.flush()
            self.denon.Zone2_SelectSourceSyncWithMainZone()
        elif input == "301*":
            sys.stdout.write("SourceSelectCommand: Selects input source zone 2 and Main zone is no longer the same\n")
            sys.stdout.flush()
            self.denon.Zone2_SelectSourceUnsyncWithMainZone()
