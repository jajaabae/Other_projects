#!/usr/bin/env python
# -*- coding: utf-8 -*-

#def fromStr_nrX(l, X):
    #l = l.replace('\n', '')
    #l = l.split('\t')
    #l = l[X-1]
#    return l

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    import re
    import unicodedata
    #value = unicode(value)
    #value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = re.sub('[-\s]+', '-', value)
    return value

def DownloadPlaylists(username, sp, IMPORT_DownloadAPlaylist):
        print 'DownloadPlaylists'
        exec IMPORT_DownloadAPlaylist
        from m.generalFunctions.fromStr_nrX import fromStr_nrX
        
        
        f = open('db/playlistsList.txt', 'r')
        lines = f.readlines()
        f.close()

        #from DownloadAPlaylist import DownloadAPlaylist
        
        #DownloadAPlaylist(username, sp, '2Nh3n4NbnJDKkuplF2R2iG')

        tmp_download = True
        for l in lines:
                PLcode = fromStr_nrX(l, 1)
                if tmp_download:
                        playlistName = fromStr_nrX(l, 3)
                        playlistName = playlistName[0:100]
                        print 'playlistName:', playlistName
                        #playlistName = slugify(playlistName)
                        trackList = DownloadAPlaylist(username, sp, PLcode)
                        f = open('db/pl/plNamed/'+playlistName+'.txt', 'w')
                        g = open('db/pl/'+PLcode+'.txt', 'w')
                        for l in trackList:
                                l = l.encode('utf-8')
                                #print '', l
                                l = l+'\n'
                                f.write(l)
                                g.write(l)
                        f.close()
                        g.close()
                #tmp_download = False
        print 'end(DownloadPlaylists)'



if __name__ == '__main__':
        from m.auth.auth import getAuthToken
        import spotipy
        from m.GetUsername.GetUsername import GetUsername

        sp = spotipy.Spotify(getAuthToken())
        username = GetUsername()
        DownloadPlaylists(username, sp, 'from DownloadAPlaylist import DownloadAPlaylist')

