def ifAndroid():
    import os
    import platform
    if platform.system() == 'Linux':
        androidDir='/storage/emulated/0/com.hipipal.qpyplus/scripts/01_effective/API_Spotify/ModularSpotifyInterface/Modules/' 
        os.chdir( androidDir)
        print os.getcwd() 
ifAndroid()

from m.getPlaylistCodeFromName.getPlaylistCodeFromName import getPlaylistCodeFromName
print getPlaylistCodeFromName('TopZouk')

