def ifAndroid():
    import os
    import platform
    if platform.system() == 'Linux':
        androidDir='/storage/emulated/0/com.hipipal.qpyplus/scripts/01_effective/API_Spotify/ModularSpotifyInterface/Modules/' 
        os.chdir( androidDir)
        print os.getcwd() 
ifAndroid()

 
from m.logger.logger import empty_log

empty_log()

#from m.logger.logger import logger 
#logger('testError', 'thisIsTheErrorWorking') 
#logger('testError', 'thisIsTheErrorWorkingWith2ndLine') 

