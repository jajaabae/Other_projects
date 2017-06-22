
def ifAndroid():
    import os
    import platform
    if platform.system() == 'Linux':
        androidDir='/storage/emulated/0/com.hipipal.qpyplus/scripts/01_effective/API_Spotify/ModularSpotifyInterface/Modules/' 
        os.chdir( androidDir)
        print os.getcwd() 
ifAndroid()


from m.auth.auth import getAuthToken
import spotipy
from m.GetUsername.GetUsername import GetUsername

#import DownloadPlaylists
#reload(DownloadPlaylists)
from m.download.DownloadPlaylists import DownloadPlaylists


import m.DownloadAPlaylist.DownloadAPlaylist
reload(m.DownloadAPlaylist.DownloadAPlaylist)
IMPORT_DownloadAPlaylist = 'from m.DownloadAPlaylist.DownloadAPlaylist import DownloadAPlaylist'

#import m.generalFunctions.fromStr_nrX
#reload(m.generalFunctions.fromStr_nrX)


sp = spotipy.Spotify(getAuthToken())
username = GetUsername()
DownloadPlaylists(username, sp, IMPORT_DownloadAPlaylist)



