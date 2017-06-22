def ifAndroid():
    import os
    import platform
    if platform.system() == 'Linux':
        androidDir='/storage/emulated/0/com.hipipal.qpyplus/scripts/01_effective/API_Spotify/ModularSpotifyInterface/Modules/' 
        os.chdir( androidDir)
        print os.getcwd() 
ifAndroid()



def ifAndroidOld():
    import os 
    print os.name
    #posix 
    import platform
    print platform.system() 
    platform.release() 
    #'2.6.22-15-generic'
    
    if platform.system() == 'Linux':
        androidDir='/storage/emulated/0/com.hipipal.qpyplus/scripts/04_examples/' 
        print androidDir
    #    androidDir='/'
        os.chdir( androidDir) 
    else:
        1==1
    print os.getcwd() 
    #exit() t() 