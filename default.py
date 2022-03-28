# Qlock screensaver add-on by phil65, adapted to Matrix by PvD
# credits to donabi, amet & phil65

import os
import sys
import xbmcgui
import xbmcaddon
import xbmcvfs

__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__cwd__ = __addon__.getAddonInfo('path')
__resource__ = xbmcvfs.translatePath(os.path.join(__cwd__, 'resources', 'lib'))

sys.path.append(__resource__)
win = xbmcgui.Window(10000)
luminance = ['cc000000', 'cc111111', 'cc222222', 'cc333333', 'cc444444', 'cc555555', 'cc666666', 'cc777777', 'cc888888']

if __name__ == '__main__':

    win.setProperty('Qlock.luminance', luminance[int(__addon__.getSetting('luminance'))])
    if win.getProperty('Qlock.colorpicker'):
        __addon__.setSetting('color', win.getProperty('Qlock.colorpicker'))
        win.clearProperty('Qlock.colorpicker')

    win.setProperty('Qlock.color', __addon__.getSetting('color'))

    from resources.lib.gui import Screensaver
    screensaver_gui = Screensaver('script-python-qlock.xml', __cwd__, 'default')
    screensaver_gui.doModal()
