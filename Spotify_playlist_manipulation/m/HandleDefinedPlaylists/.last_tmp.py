def getArgumentsFromDefinedPLFile(defPLFile):
    f = open(defPLFile, 'r')
    lines = f.readlines()
    f.close()
    PLArgSets = lines
    return PLArgSets

def splitArgSets(PLArgSetsList):
    #print 'PLArgSetsList', PLArgSetsList
    argGroups = []
    aGroup=[]
    for a in PLArgSetsList:
        a = a.replace('\xef','').replace('\xbb','').replace('\xbf','')
        a = a.replace('\n','').replace('\r','')
        #print a
        if a == '{endArg}':
            argGroups.append(aGroup)
            aGroup=[]
        else:
            aGroup+=[a]
    argGroups.append(aGroup)
    #print 'argGroups', argGroups
    return argGroups
    
def handleArgSet(argSet):
    result = None
    print
    print 'argSet', argSet
    print 'argSet', len(argSet)
    #+ and -
    grWith = []
    grWithout = []
    for a in argSet:
        if len(a)>0:
            if a[0] == '-':
                grWithout.append( a[1:] )
            else:
                grWith.append( a )
    from m.getPlaylistCodeFromName.getPlaylistCodeFromName import getPlaylistCodeFromName
    #from m.getPlaylistFromName.getPlaylistFromName import getPlaylistFromName
    #getPlaylistCodeFromName()
    
    from m.auth.auth import getAuthToken
    import spotipy
    from m.GetUsername.GetUsername import GetUsername
    from m.DownloadAPlaylist.DownloadAPlaylist import DownloadAPlaylist
    sp = spotipy.Spotify(getAuthToken())
    #trackList = DownloadAPlaylist(GetUsername(), sp, pl)
    
    songListWith = []
    for pl in grWith:
        pl_code = getPlaylistCodeFromName(pl)
        songListWith += DownloadAPlaylist(GetUsername(), sp, pl_code)
    songListWithout = []
    for pl in grWithout:
        pl_code = getPlaylistCodeFromName(pl)
        songListWithout += DownloadAPlaylist(GetUsername(), sp, pl_code)
    #"""
    
    #+ without -
    print len(set(songListWith))
    print len(set(songListWithout))
    result = list(set(songListWith)-set(songListWithout))
    print len(result)
    
    #unique
    result = set(result)

    #print 'result', result
    return result

def writePlaylist(pl_name_n_path, songs):
    pl_name = pl_name_n_path.split('/')[-1]
    print pl_name
    
    import os
    d = '/'.join(pl_name_n_path.split('/')[0:-1])+'/'
    print d
    d = d.replace('db/definedPL', 'db/definedPL_generated')
    print d
    print(os.path.isdir(d))

    #if not os.path.isdir(d):
    try:
        os.stat(d)
    except:
        os.mkdir(d)
    
    #f = open('db/definedPL_generated/'+pl_name, 'w')
    out_pl_name_n_path = pl_name_n_path.replace('db/definedPL', 'db/definedPL_generated')
    f = open(out_pl_name_n_path, 'w')
    o = open(out_pl_name_n_path.replace('.txt', '.SPL'), 'w')
    for s in songs:
        s = s.encode('utf-8')
        f.write('https://open.spotify.com/track/'+s+'\n')
        s = s.split('\t')[0]
        o.write('https://open.spotify.com/track/'+s+'\n')
    f.close()
    o.close()



def generateDefinedPlaylist( defPLFile ):
    pl_name = defPLFile
    pl_name_n_path = defPLFile
    pl_name = pl_name.split('/')[-1]
    print
    print 'start', pl_name
    PLArgSetsList = getArgumentsFromDefinedPLFile(defPLFile)
    PLArgSets = splitArgSets(PLArgSetsList)
    songs = []
    for argSet in PLArgSets:
        print 'argSet', argSet
        songs += handleArgSet(argSet)
    songs = list(set(songs))
    writePlaylist(pl_name_n_path, songs)
    print 'end(', pl_name, ')'


def uploadPlaylistOnline( plCode, tracks ):
    #print plCode
    #print len(tracks)
    #user_playlist_replace_tracks(user,playlist_id, tracks)
    from m.auth.auth import getAuthToken
    import spotipy
    from m.GetUsername.GetUsername import GetUsername
    sp = spotipy.Spotify(getAuthToken())
    sp.user_playlist_replace_tracks( GetUsername() , plCode, tracks )
    
    
def uploadPlaylist( defPLFile ):
    pl_name_n_path = defPLFile
    pl_name = defPLFile.split('/')[-1].replace('.txt', '')
    generatedInPath = pl_name_n_path.replace('definedPL', 'definedPL_generated')
    #print generatedInPath
    print pl_name
    f = open (generatedInPath, 'r')
    tracks = []
    for l in f:
        tracks.append(l.split('\t')[0])
    f.close()
    #print lines
    from m.getPlaylistCodeFromName.getPlaylistCodeFromName import getPlaylistCodeFromName
    plCode = getPlaylistCodeFromName( pl_name )
    if not plCode == None:
        print '* Uploading:', pl_name
        uploadPlaylistOnline(plCode, tracks)
        print '* done'
    else:
        print '* not uploaded:', pl_name
    

def HandleDefinedPlaylists():
    #01 GetArgumentFiles
    from m.HandleDefinedPlaylists.Digg_definedPL import Digg_definedPL
    definedPLs = Digg_definedPL()

    #02 GetArgumentsFrom each DefinedPLFile
    #print 'definedPLs', definedPLs
    for defPLFile in definedPLs:
        #print defPLFile
        generateDefinedPlaylist( defPLFile )
        #uploadPlaylist( defPLFile )
        







if __name__ == '__main__':
    def ifAndroid():
        import os
        import platform
        if platform.system() == 'Linux':
            androidDir='/storage/emulated/0/com.hipipal.qpyplus/scripts/01_effective/API_Spotify/ModularSpotifyInterface/Modules/' 
            os.chdir( androidDir) 
            print os.getcwd() 
    ifAndroid()

    HandleDefinedPlaylists()