#!/usr/bin/env python
# -*- coding: utf-8 -*-


def show_tracks(results):
    tracks = results
    lines = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
        ###print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])
        trackID = track['id']
        trackName = track['name']
        trackArtist = track['artists'][0]['name']
        #print trackID, trackName, '-', trackArtist
        lines += [trackID+'\t'+trackName+' - '+trackArtist]
    return lines


def DownloadAPlaylist(username, sp, playlistID):
        
        ##playlist = sp.user_playlist(user, playlist_id='2Nh3n4NbnJDKkuplF2R2iG', fields=None)
        #playlist = sp.user_playlist(username, playlistID, fields="tracks,next")
        ##print playlist['tracks']
        ##print playlist


        print 'playlistID: ', playlistID
        #playlist = sp.user_playlist(username, playlistID, fields="tracks,next")
        #tracks = playlist['tracks']
        #print type(tracks)
        #print tracks

        results = sp.user_playlist(username, playlistID, fields="tracks,next")
        tracks = results['tracks']
        trackList = show_tracks(tracks)
        for l in trackList:
            print l
        #print '-'
        #while tracks['next']:
        #    tracks = sp.next(tracks)
        #    show_tracks(tracks)
        #print '-'
        





if __name__ == '__main__':
        from m.auth.auth import getAuthToken
        import spotipy
        from m.GetUsername.GetUsername import GetUsername

        sp = spotipy.Spotify(getAuthToken())
        username = GetUsername()
        DownloadPlaylists(username, sp)

