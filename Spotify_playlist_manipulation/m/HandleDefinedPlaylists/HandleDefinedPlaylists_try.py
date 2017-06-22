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
    from m.DownloadAPlaylist.DownloadAPlaylist import DownloadAPlaylist #redundant?
    import m.db_Requests.db_GetAPlaylist#
    reload(m.db_Requests.db_GetAPlaylist)#
    from m.db_Requests.db_GetAPlaylist import db_GetAPlaylist
    sp = spotipy.Spotify(getAuthToken())
    #trackList = DownloadAPlaylist(GetUsername(), sp, pl)
    
    songListWith = []
    #songListWith2 = []
    for pl in grWith:
        pl_code = getPlaylistCodeFromName(pl)
        try:
            songListWith += DownloadAPlaylist(GetUsername(), sp, pl_code)
            #songListWith += db_GetAPlaylist(GetUsername(), pl_code)
        except:
            print '******** ERROR *******'
            print '*',pl
            print '**', pl_code
            print '**********************'
        
        #print '*'
        #print DownloadAPlaylist(GetUsername(), sp, pl_code)
        #print db_GetAPlaylist(GetUsername(), sp, pl_code)
        #print '*end'
    songListWithout = []
    for pl in grWithout:
        pl_code = getPlaylistCodeFromName(pl)
        print '*',pl
        print '**', pl_code
        try:
            songListWith += DownloadAPlaylist(GetUsername(), sp, pl_code)
            #print DownloadAPlaylist(GetUsername(), sp, pl_code)
            #songListWith += db_GetAPlaylist(GetUsername(), pl_code)
        except:
            print '******** ERROR *******'
            print '*',pl
            print '**', pl_code
            print '**********************'
    #"""
        
    #print '****'
    #print type(songListWith)
    #try:
    #    print type(songListWith[0])
    #except:
    #    pass
    #print songListWith
    #print '---------------'
    #print type(songListWith2)
    #try:
    #    print type(songListWith2[0])
    #except:
    #    pass
    #print songListWith2
    #print 'EEEEEEEEEEEEEEEEEEEE'
    

    
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


def grouper(n, iterable, fillvalue=None): 
    from itertools import izip_longest 
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx" 
    args = [iter(iterable)] * n 
    return izip_longest(fillvalue=fillvalue, *args) 
    i = grouper(50,range(100))
    
def uploadPlaylistOnline( plCode, tracks ):
    #print plCode
    #print len(tracks)
    #user_playlist_replace_tracks(user,playlist_id, tracks)
    from m.auth.auth import getAuthToken
    import spotipy
    from m.GetUsername.GetUsername import GetUsername
    sp = spotipy.Spotify(getAuthToken())

#    i = grouper(50,range(100))
#    for k in i:
#        print k
#    sp.user_playlist_replace_tracks( GetUsername() , plCode, ['https://open.spotify.com/track/79VrLhKslMZnzlfyVPtgSP'] )    
    sp.user_playlist_replace_tracks( GetUsername() , plCode, [])
    i = grouper(50,tracks)
    for k in i:
        #print k
        k=filter(None,k)
        sp. user_playlist_add_tracks(GetUsername(), plCode, k, position=None)
    
    
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
#    if not plCode == None and pl_name=='out_zoukGood_verified' :
#    if not plCode == None:
#    print pl_name[0:4]
    if not plCode == None and 'out_' == pl_name[0:4]:
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
        uploadPlaylist( defPLFile )
        







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
