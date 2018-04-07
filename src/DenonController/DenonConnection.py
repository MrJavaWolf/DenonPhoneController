import socket
import DenonCommands
import time
import sys
import traceback


class DenonConnection:

    def __init__(self, ip, port, errorCallback):
        self.Ip = ip
        self.Port = port
        self.ErrorCallback = errorCallback
        self.IsConnected = False
        self.Connect()

    def Connect(self):
        while self.IsConnected == False:
            try:
                self.denonSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.denonSocket.connect((self.Ip, self.Port))
                self.denonSocket.settimeout(5)
                self.IsConnected = True
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception as e:
                sys.stdout.write(traceback.format_exc())
                sys.stdout.write("\n")
                sys.stdout.flush()
                self.ErrorCallback()
                time.sleep(5)

    def SendMessage(self, message):
        isSend = False
        while isSend == False:
            try:
                #Sends the actual message
                self.denonSocket.send(str.encode(message))
                isSend = True
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception as e:
                sys.stdout.write(traceback.format_exc())
                sys.stdout.write("\n")
                sys.stdout.flush()
                self.ErrorCallback()
                time.sleep(5)
                self.Close()
                self.Connect()
        #Enforce a 50 ms wait, the Denon will not accept more than 1 commnd
        #every 50 ms
        time.sleep(0.05)
    
    def WaitForResponse(self, possibleResponses):
        denonResponseBytes = b''
        while True:    
            denonResponseBytes += self.denonSocket.recv(1024)
            denonResponse = denonResponseBytes.decode("ascii")
            for possibleResponse in possibleResponses:
                if possibleResponse in denonResponse: 
                    return denonResponseBytes

    def Close(self):
        try:
            self.denonSocket.close()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            #swallow
            a = 0 

    def SetMasterVolume(self, volume):
        self.SendMessage(DenonCommands.SetVolume(volume))
        self.WaitForResponse(["\r"])

    def IsPoweredOn(self):
        self.SendMessage(DenonCommands.GetPowerStatus)
        responseBytes = self.WaitForResponse([DenonCommands.PowerOn, DenonCommands.PowerOff])
        response = responseBytes.decode("ascii")
        if DenonCommands.PowerOn in response:
            return True
        else: 
            return False

    def PowerOn(self):
        if self.IsPoweredOn():
            return
        else:
            self.SendMessage(DenonCommands.PowerOn)
        self.WaitForResponse(["\r"])
    
    def PowerOff(self):
        if self.IsPoweredOn():
            self.SendMessage(DenonCommands.PowerOff)
        self.WaitForResponse(["\r"])
    
    def IsMuted(self):
        self.SendMessage(DenonCommands.GetMuteStatus)
        responseBytes = self.WaitForResponse([DenonCommands.MuteOn, DenonCommands.MuteOff])
        response = responseBytes.decode("ascii")
        if DenonCommands.MuteOn in response:
            return True
        else: 
            return False
        
    def MuteOn(self):
        self.SendMessage(DenonCommands.MuteOn)
        self.WaitForResponse(["\r"])

    def MuteOff(self):
        self.SendMessage(DenonCommands.MuteOff)
        self.WaitForResponse(["\r"])


    def IsZone2PoweredOn(self):
        self.SendMessage(DenonCommands.Zone2_Status)
        responseBytes = self.WaitForResponse([DenonCommands.Zone2_On, DenonCommands.Zone2_Off])
        response = responseBytes.decode("ascii")
        if DenonCommands.Zone2_On in response:
            return True
        else: 
            return False

    def SelectSourcePhone(self):
        self.SendMessage(DenonCommands.SelectSourcePhone)
        self.WaitForResponse(["\r"])

    def SelectSourceCD(self):
        self.SendMessage(DenonCommands.SelectSourceCD)
        self.WaitForResponse(["\r"])

    def SelectSourceTuner(self):
        self.SendMessage(DenonCommands.SelectSourceTuner)
        self.WaitForResponse(["\r"])

    def SelectSourceDVD(self):
        self.SendMessage(DenonCommands.SelectSourceDVD)
        self.WaitForResponse(["\r"])

    def SelectSourceBD(self):
        self.SendMessage(DenonCommands.SelectSourceBD)
        self.WaitForResponse(["\r"])

    def SelectSourceTV(self):
        self.SendMessage(DenonCommands.SelectSourceTV)
        self.WaitForResponse(["\r"])

    def SelectSourceSATCBL(self):
        self.SendMessage(DenonCommands.SelectSourceSATCBL)
        self.WaitForResponse(["\r"])

    def SelectSourceDVR(self):
        self.SendMessage(DenonCommands.SelectSourceDVR)
        self.WaitForResponse(["\r"])

    def SelectSourceGame(self):
        self.SendMessage(DenonCommands.SelectSourceGame)
        self.WaitForResponse(["\r"])

    def SelectSourceGame2(self):
        self.SendMessage(DenonCommands.SelectSourceGame2)
        self.WaitForResponse(["\r"])

    def SelectSourceVAUX(self):
        self.SendMessage(DenonCommands.SelectSourceVAUX)
        self.WaitForResponse(["\r"])

    def SelectSourceDock(self):
        self.SendMessage(DenonCommands.SelectSourceDock)
        self.WaitForResponse(["\r"])

    def SelectSourceIPod(self):
        self.SendMessage(DenonCommands.SelectSourceIPod)
        self.WaitForResponse(["\r"])

    def SelectSourceNetUSB(self):
        self.SendMessage(DenonCommands.SelectSourceNetUSB)
        self.WaitForResponse(["\r"])

    def SelectSourceNapster(self):
        self.SendMessage(DenonCommands.SelectSourceNapster)
        self.WaitForResponse(["\r"])

    def SelectSourceLastFM(self):
        self.SendMessage(DenonCommands.SelectSourceLastFM)
        self.WaitForResponse(["\r"])

    def SelectSourceFlicker(self):
        self.SendMessage(DenonCommands.SelectSourceFlicker)
        self.WaitForResponse(["\r"])

    def SelectSourceFavorites(self):
        self.SendMessage(DenonCommands.SelectSourceFavorites)
        self.WaitForResponse(["\r"])

    def SelectSourceInternetRadio(self):
        self.SendMessage(DenonCommands.SelectSourceInternetRadio)
        self.WaitForResponse(["\r"])

    def SelectSourceServer(self):
        self.SendMessage(DenonCommands.SelectSourceServer)
        self.WaitForResponse(["\r"])

    def SelectSourceUSBIPod(self):
        self.SendMessage(DenonCommands.SelectSourceUSBIPod)
        self.WaitForResponse(["\r"])

    def SelectSourceUSB(self):
        self.SendMessage(DenonCommands.SelectSourceUSB)
        self.WaitForResponse(["\r"])

    def SelectSourceIPD(self):
        self.SendMessage(DenonCommands.SelectSourceIPD)
        self.WaitForResponse(["\r"])

    def SelectSourceIRP(self):
        self.SendMessage(DenonCommands.SelectSourceIRP)
        self.WaitForResponse(["\r"])

    def SelectSourceFVP(self):
        self.SendMessage(DenonCommands.SelectSourceFVP)
        self.WaitForResponse(["\r"])
        
    def Zone2PowerOn(self):
        if self.IsZone2PoweredOn():
            return
        else:
            self.SendMessage(DenonCommands.Zone2_On)
            self.WaitForResponse(["\r"])

    def Zone2PowerOff(self):
        if self.IsZone2PoweredOn():
            self.SendMessage(DenonCommands.Zone2_Off)
            self.WaitForResponse(["\r"])

    def SetZone2Volume(self, volume):
        self.SendMessage(DenonCommands.Zone2_SetVolume(volume))
        self.WaitForResponse(["\r"])

    def Zone2IsMuted(self):
        self.SendMessage(DenonCommands.Zone2_GetMuteStatus)
        responseBytes = self.WaitForResponse([DenonCommands.Zone2_MuteOn, DenonCommands.Zone2_MuteOff])
        response = responseBytes.decode("ascii")
        if Zone2_MuteOn in response:
            return True
        else: 
            return False
        
    def Zone2MuteOn(self):
        self.SendMessage(DenonCommands.Zone2_MuteOn)
        self.WaitForResponse(["\r"])

    def Zone2MuteOff(self):
        self.SendMessage(DenonCommands.Zone2_MuteOff)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourcePhone(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourcePhone)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceCD(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceCD)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceTuner(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceTuner)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceDVD(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceDVD)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceBD(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceBD)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceTV(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceTV)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceSATCBL(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceSATCBL)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceDVR(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceDVR)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceGame(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceGame)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceGame2(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceGame2)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceVAUX(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceVAUX)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceDock(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceDock)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceIPod(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceIPod)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceNetUSB(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceNetUSB)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceNapster(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceNapster)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceLastFM(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceLastFM)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceFlicker(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceFlicker)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceFavorites(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceFavorites)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceInternetRadio(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceInternetRadio)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceServer(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceServer)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceUSBIPod(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceUSBIPod)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceUSB(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceUSB)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceIPD(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceIPD)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceIRP(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceIRP)
        self.WaitForResponse(["\r"])

    def Zone2_SelectSourceFVP(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceFVP)
        self.WaitForResponse(["\r"])
        
    def Zone2_SelectSourceSyncWithMainZone(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceMainZone)
        res = self.WaitForResponse(["\r"])
    
    def Zone2_SelectSourceUnsyncWithMainZone(self):
        self.SendMessage(DenonCommands.Zone2_SelectSourceDeselectMainZone)
        res = self.WaitForResponse(["\r"])