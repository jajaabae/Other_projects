#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from m.cleanDir.removeFilesInDir import removeFilesInDir

def empty_log():
    path = 'db/log/'
    removeFilesInDir(path)

"""
def empty_log_old():
    import os
    path = 'db/log/'
    liste=[]
    try:
        liste=os.listdir(path)
    except:
        pass
    for d in liste:
        os.remove(path+d)
        print 'removed:', d
#"""

def addLineToFile( fileNameInPath, l):
    makeFileExist( fileNameInPath )
    f=open( fileNameInPath ,'r')
    lines = f.readlines()
    lines += l+'\n'
    f.close()
    
    lines = ''.join(lines)
    
    f=open( fileNameInPath ,'w')
    f.write(lines)
    f.close() 
    
def makeFileExist( fileNameInPath ):
    import os.path
    if not os.path.isfile( fileNameInPath ):
        f=open( fileNameInPath ,'w')
        f.write('') 
        f.close()
    
def reduceFileToUniqueLines():
    pass 
def logger(errortype, errorMsg):
    fileNameInPath = 'db/log/'+errortype+'.txt'
    l=errorMsg+'\n'
    addLineToFile( fileNameInPath, l)
    
empty_log()
