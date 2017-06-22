#import m.cleanDir.removeFilesInDir
#reload(m.cleanDir.removeFilesInDir)
from m.cleanDir.removeFilesInDir import removeFilesInDir

def afterCleaning():
    removeFilesInDir('db/pl/')
    removeFilesInDir('db/pl/plNamed/')

afterCleaning()
