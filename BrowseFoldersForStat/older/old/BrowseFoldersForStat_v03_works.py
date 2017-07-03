import os
from os.path import join, getsize, isfile, isdir, splitext

dirPath = "C:/"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup/programming/python"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup/XperiaConBckQpyFolderScripts/PC"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup"

dirPath = 'storage/sdcard0/com.hipipal.qpyplus' 
dirPath = 'storage/sdcard0' 

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



def pf(subNR, size, name, path):
    tab="|"
    i=0
    while i<subNR:
        tab=tab+"-"
        i=i+1
    if subNR==0:
        tab="*"
    if bToMb(size)>1:
        #print tab+" "+str(bToMb(size))+" "+name+" \n\t("+path+")"
        print tab+" "+str(bToMb(size))+" Mb  "+name



def bToMb(b):
    return b/1024/1024
    #return b #bytes


    
def folderDigger(parNR, directory, name):
    size = 0
    subNR = parNR+1
    
    for folder in os.listdir(directory):
        if os.path.isdir(directory+"/"+folder):
            size = size + folderDigger(subNR, (directory+"/"+folder), folder)
        
    for fil in os.listdir(directory):
        if os.path.isfile(directory+"/"+fil):
            size = size+getsize(directory+"/"+fil)
            pf(subNR+1, getsize(directory+"/"+fil), fil, directory)
    
    pf(subNR, size, name, directory)
    return size
    
    
    
folderDigger(-1, dirPath, dirPath)



#print bToMb(TotalSize)




