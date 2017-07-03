import os
from os.path import join, getsize, isfile, isdir, splitext

dirPath = "C:/"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup/programming/python"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup/XperiaConBckQpyFolderScripts/PC"
#dirPath = 'storage/sdcard0/com.hipipal.qpyplus/scripts/PyIOFolder'

#os.chdir(dirPath)
#print os.getcwd()


def tmp():
    TotalSize = 0
    for item in os.walk(dirPath):
        for file in item[2]:
            try:
                TotalSize = TotalSize + getsize(join(item[0], file))
            except:
                print("error with file:  " + join(item[0], file))

#print str(TotalSize)+" b"
#print str(TotalSize/1024)+" kb"
#print str(TotalSize/1024/1024)+" Mb"
#print str(TotalSize /1024 /1024 /1024)+" Gb"

print "----"



def pf(subNR, size, name):
    tab="|"
    i=0
    while i<subNR:
        tab=tab+"-"
        i=i+1
    print tab+" "+str(bToMb(size))+" "+name



def bToMb(b):
    #return b/1024/1024
    return b


    
def folderDigger(parNR, directory, name):
    size = 0
    subNR = parNR+1
    
    #for "folders":
        #folderDigger(parNR, directory, name)
        
    for fil in os.listdir(directory):
        if os.path.isfile(directory+"/"+fil):
            size = size+getsize(directory+"/"+fil)
    
    pf(subNR, size, name)
    return size
    
    
    
folderDigger(-1, dirPath, "main")



#print bToMb(TotalSize)




