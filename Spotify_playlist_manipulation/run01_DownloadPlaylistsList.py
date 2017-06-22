def ifAndroid():
    import os
    import platform
    if platform.system() == 'Linux':
        androidDir='/storage/emulated/0/com.hipipal.qpyplus/scripts/01_effective/API_Spotify/ModularSpotifyInterface/Modules/' 
        os.chdir( androidDir)
        print os.getcwd() 
ifAndroid()

from m.auth.auth import getAuthToken
from m.GetUsername.GetUsername import GetUsername
import spotipy

import m.download.DownloadPlaylistList
reload(m.download.DownloadPlaylistList)

from m.download.DownloadPlaylistList import DownloadPlaylistList




sp = spotipy.Spotify(getAuthToken())
username = GetUsername()
DownloadPlaylistList(sp, username)


