import os
from os.path import join, getsize, isfile, isdir, splitext

dirPath = "C:/"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup/programming/python"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup/XperiaConBckQpyFolderScripts/PC"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup"

#dirPath = 'storage/sdcard0/com.hipipal.qpyplus' 
#dirPath = 'storage/sdcard0' 



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
    global BadOnes
    BadOnes=""

    size = 0
    subNR = parNR+1
    
    for item in os.listdir(directory):
        if not os.path.isdir(directory+"/"+item):
            if os.path.isfile(directory+"/"+item):
#                global BadOnes
                BadOnes= BadOnes+"\n"+item+" ("+directory+")"
    
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
print BadOnes


#print bToMb(TotalSize)




