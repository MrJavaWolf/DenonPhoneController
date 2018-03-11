# All commands can be found here:
# http://openrb.com/wp-content/uploads/2012/02/AVR3312CI_AVR3312_PROTOCOL_V7.6.0.pdf
EndTag = "\r"

#Power control
PowerOn = "PWON" + EndTag
PowerOff = "PWSTANDBY" + EndTag
GetPowerStatus = "PW?" + EndTag

#Volume control
VolumeUp = "MVUP" + EndTag
VolumeDown = "MVDOWN" + EndTag
GetVolume = "MV?" + EndTag
MuteOn = "MUON" + EndTag
MuteOff = "MUOFF" + EndTag
GetMuteStatus = "MU?" + EndTag
def SetVolume(volume):
    return "MV" + volume + EndTag

#Selected Source Control
SelectSourcePhone = "SIPHONO " + EndTag
SelectSourceCD = "SICD" + EndTag
SelectSourceTuner = "SITUNER" + EndTag
SelectSourceDVD = "SIDVD" + EndTag
SelectSourceBD = "SIBD" + EndTag
SelectSourceTV = "SITV" + EndTag
SelectSourceSATCBL = "SISAT/CBL" + EndTag
SelectSourceDVR = "SIDVR" + EndTag
SelectSourceGame = "SIGAME" + EndTag
SelectSourceGame2 = "SIGAME2" + EndTag
SelectSourceVAUX = "SIV.AUX" + EndTag
SelectSourceDock = "SIDOCK" + EndTag
SelectSourceIPod = "SIIPOD" + EndTag
SelectSourceNetUSB = "SINET/USB" + EndTag
SelectSourceNapster = "SINAPSTER" + EndTag
SelectSourceLastFM = "SILASTFM" + EndTag
SelectSourceFlicker = "SIFLICKER" + EndTag
SelectSourceFavorites = "SIFAVORITES" + EndTag
SelectSourceInternetRadio = "SIIRADIO" + EndTag
SelectSourceServer = "SISERVER" + EndTag
SelectSourceUSBIPod = "SIUSB/IPOD" + EndTag
SelectSourceUSB = "SIUSB" + EndTag
SelectSourceIPD = "SIIPD" + EndTag
SelectSourceIRP = "SIIRP" + EndTag
SelectSourceFVP = "SIFVP" + EndTag


# - - - - - ZONE 2 - - - - - #
Zone2_VolumeUp = "Z2UP" + EndTag
Zone2_VolumeDown = "Z2DOWN" + EndTag

Zone2_On = "Z2ON" + EndTag
Zone2_Off = "Z2OFF" + EndTag
Zone2_Status = "Z2?" + EndTag

Zone2_MuteOn = "Z2MUON" + EndTag
Zone2_MuteOff = "Z2MUOFF" + EndTag
Zone2_GetMuteStatus = "MU?" + EndTag
def Zone2_SetVolume(volume):
    return "Z2" + volume + EndTag

Zone2_SelectSourceMainZone = "MNZST ON" + EndTag
Zone2_SelectSourceDeselectMainZone = "MNZST OFF" + EndTag
Zone2_SelectSourceBluetooth = "Z2BT" + EndTag
Zone2_SelectSourcePhone = "Z2PHONO " + EndTag
Zone2_SelectSourceCD = "Z2CD" + EndTag
Zone2_SelectSourceTuner = "Z2TUNER" + EndTag
Zone2_SelectSourceDVD = "Z2DVD" + EndTag
Zone2_SelectSourceBD = "Z2BD" + EndTag
Zone2_SelectSourceTV = "Z2TV" + EndTag
Zone2_SelectSourceSATCBL = "Z2SAT/CBL" + EndTag
Zone2_SelectSourceDVR = "Z2DVR" + EndTag
Zone2_SelectSourceGame = "Z2GAME" + EndTag
Zone2_SelectSourceGame2 = "Z2GAME2" + EndTag
Zone2_SelectSourceVAUX = "Z2V.AUX" + EndTag
Zone2_SelectSourceDock = "Z2DOCK" + EndTag
Zone2_SelectSourceIPod = "Z2IPOD" + EndTag
Zone2_SelectSourceNetUSB = "Z2NET/USB" + EndTag
Zone2_SelectSourceNapster = "Z2NAPSTER" + EndTag
Zone2_SelectSourceLastFM = "Z2LASTFM" + EndTag
Zone2_SelectSourceFlicker = "Z2FLICKER" + EndTag
Zone2_SelectSourceFavorites = "Z2FAVORITES" + EndTag
Zone2_SelectSourceInternetRadio = "Z2IRADIO" + EndTag
Zone2_SelectSourceServer = "Z2SERVER" + EndTag
Zone2_SelectSourceUSBIPod = "Z2USB/IPOD" + EndTag
Zone2_SelectSourceUSB = "Z2USB" + EndTag
Zone2_SelectSourceIPD = "Z2IPD" + EndTag
Zone2_SelectSourceIRP = "Z2IRP" + EndTag
Zone2_SelectSourceFVP = "Z2FVP" + EndTag


