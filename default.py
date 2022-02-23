# Qlock screensaver add-on by phil65, adapted to Matrix by PvD
# credits to donabi, amet & phil65

import os
import sys
import xbmcaddon
import xbmcvfs

__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__cwd__ = __addon__.getAddonInfo('path')
__resource__ = xbmcvfs.translatePath(os.path.join(__cwd__, 'resources', 'lib'))

sys.path.append(__resource__)

if __name__ == '__main__':
    from resources.lib.gui import Screensaver
    screensaver_gui = Screensaver('script-python-qlock.xml', __cwd__, 'default')
    screensaver_gui.doModal()
