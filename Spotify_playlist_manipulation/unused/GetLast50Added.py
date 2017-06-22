
def GetLast50Added(sp):
    #import spotipy
    
    
        #sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks('50')
        for item in results['items']:
            track = item['track']
            try:
                print track['name'] + ' - ' + track['artists'][0]['name']
            except:
                print '# print error' 


if __name__ == '__main__':
        from auth.auth import getAuthToken
        import spotipy
        
        sp = spotipy.Spotify(getAuthToken())
        GetLast50Added(sp)
