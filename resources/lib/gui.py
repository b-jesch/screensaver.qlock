import xbmc
import xbmcgui


class Screensaver(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        self.stop = False
        self.Monitor = MyMonitor(action=self.exit)

    def onInit(self):
        while (not self.Monitor.abortRequested()) and (not self.stop):
            xbmc.sleep(1000)

    def exit(self):
        self.stop = True
        self.close()


class MyMonitor(xbmc.Monitor):

    def __init__(self, *args, **kwargs):
        self.action = kwargs['action']

    def onScreensaverDeactivated(self):
        self.action()
