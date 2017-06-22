
from m.auth.auth import getAuthToken
import spotipy
from m.GetUsername.GetUsername import GetUsername

import m.DownloadAPlaylist.DownloadAPlaylist
reload(m.DownloadAPlaylist.DownloadAPlaylist)
IMPORT_DownloadAPlaylist = 'from m.DownloadAPlaylist.DownloadAPlaylist import DownloadAPlaylist'
exec IMPORT_DownloadAPlaylist



sp = spotipy.Spotify(getAuthToken())
username = GetUsername()


trackList = DownloadAPlaylist(username, sp, '0hWwvQU704BAA4mVOTQmvT')
for l in trackList:
    print l
print len(trackList)


