"""
#spotipy
def _warn(self, msg):
    print('warning:' + msg, file=sys.stderr)
"""



"""
# warnings module
import warnings 
def fxn(): 
    warnings.warn("deprecated", DeprecationWarning) 
with warnings.catch_warnings(): 
    warnings.simplefilter("ignore") 
    fxn()



#requests.packages.urllib3.disable_warnings()
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
"""


"""
import urllib3 
urllib3.disable_warnings()


import os 
import sys
sys.stdout = os.devnull 
sys.stderr = os.devnull
sys.stdout = sys.__stdout__ 
sys.stderr = sys.__stderr__

from contextlib import contextmanager 
import sys, os 
@contextmanager 
def suppress_stdout(): 
    with open(os.devnull, "w") as devnull: 
        old_stdout = sys.stdout 
        #sys.stdout = devnull
        sys.stderr = os.devnull
        
        try: 
            yield 
        finally: 
            sys.stdout = old_stdout

print("Now you see it") 
with suppress_stdout(): 
    print("Now you don't")
"""



def runAll():
    import run00_logger
    print '### run01_DownloadPlaylistsList ###'
    import run01_DownloadPlaylistsList
    print '### run02_DownloadPlaylists ###' 
    import run02_DownloadPlaylists
    print '### run06_generateDefinedPlaylistsists ###' 
    import run06_HandleDefinedPlaylists
    print '### end ###' 
runAll()


#with suppress_stdout():
#    runAll()



## Was ok?
#import warnings 
#def fxn(): 
#    warnings.warn("deprecated", DeprecationWarning) 
#with warnings.catch_warnings(): 
#    warnings.simplefilter("ignore") 
#    runAll()
#    fxn()