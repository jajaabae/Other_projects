#!/usr/bin/env python
# -*- coding: utf-8 -*-


def show_tracks(results):
    tracks = results
    lines = [] #[''.encode('utf-8')]
    for i, item in enumerate(tracks['items']):
        track = item['track']
        if not track==None:
            ###print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])
            trackID = track['id']
            if trackID == None:
                trackID = str(trackID)
            trackName = track['name']
            trackArtist = track['artists'][0]['name']
            #print trackID, trackName, '-', trackArtist
            #lines += [str(trackID)+'\t'+str(trackName)+'\t-\t'+str(trackArtist)]
            lines += [trackID+'\t'+trackName+'\t-\t'+trackArtist]
        else:
            print "ERROR: track['id']"
            
    return lines


def db_GetAPlaylist(username, playlistID):
        #print 'db_get playlist from playlistID:', playlistID
    
        #results = sp.user_playlist(username, playlistID, fields="tracks,next")
        #tracks = results['tracks']
        #trackList = show_tracks(tracks)
        #while tracks['next']:
        #    tracks = sp.next(tracks)
        #    trackList += show_tracks(tracks)
        #print '---------**************---------',type(trackList)
        #print trackList
        trackList = []
        if not playlistID == None:
            
            plInPath = 'db/pl/'+playlistID+'.txt'
            f = open(plInPath, 'r')
            for l in f:

                l = l.split('\t')[0]
                l=l+'\t' #### !!! BAD SOLUTION !!!
                l=l.encode('utf-8')
                #print type(l)
                #trackList += [l.encode('utf-8')]
                
                trackList += [l]
            f.close()
        #print '---------TTTTTTTTTTTTTTTT---------',type(trackList)
        #print trackList
        #for l in trackList:
        #    print l

        #print 'end(db_get playlist from playlistID:', playlistID, ')'
        return trackList




if __name__ == '__main__':
        from m.auth.auth import getAuthToken
        import spotipy
        from m.GetUsername.GetUsername import GetUsername

        sp = spotipy.Spotify(getAuthToken())
        username = GetUsername()
        DownloadPlaylists(username, sp)

