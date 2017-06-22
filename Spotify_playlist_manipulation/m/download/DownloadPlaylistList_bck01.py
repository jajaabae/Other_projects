#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from GetUsername import GetUsername
#from GetUsername.GetUsername import GetUsername
def DownloadPlaylistList(sp, username):
    
        #playlists = sp.user_playlists(username, 1, 53)
        #playlists = sp.user_playlists(username, 1, 1)
        
        playlists1 = sp.user_playlists(username, 50, 0)
        playlists2 = sp.user_playlists(username, 50, 50)
        playlists3 = sp.user_playlists(username, 50, 100)
        
        
        #print playlists
        #print type(playlists)
        #print type(playlists['items'])
        #print len(playlists['items'])
        #print playlists['items'][1]
        #print playlists['items'][49]
        playlists = playlists1['items']+playlists2['items']+playlists3['items']


        """
        i=0
        notExausted = True
        while notExausted:
                playlistDict = sp.user_playlists(username, 1, i)
                notExausted = False

        #"""



        
        #print
        #playlists = playlists['next']
        #print playlists
        
        f = open('db/playlistsList.txt', 'w')
        print 'downloading playlist-list'
        #for playlist in playlists['items']:
        for playlist in playlists:
            if playlist['owner']['id'] == username:
                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                #tracks = results['tracks']
                
                string = playlist['id'] +'\t'+ str(playlist['tracks']['total']) +'\t'+ playlist['name'] +'\n'
                s = string.encode('utf-8')
                f.write(s)
                #print s.decode('utf-8').replace('\n', '')
        f.close()
        print 'end(downloading playlist-list)'
        






if __name__ == '__main__':
        from m.auth.auth import getAuthToken
        from m.GetUsername.GetUsername import GetUsername
        import spotipy
        sp = spotipy.Spotify(getAuthToken())
        username = GetUsername()
        DownloadPlaylistList(sp, username)



