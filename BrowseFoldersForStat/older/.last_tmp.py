import os
from os.path import join, getsize, isfile, isdir, splitext
from decimal import Decimal



############################
######### Settings #########
############################
print os.getcwd()
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup"
dirPath = "C:/"
dirPath = "C:/Users/Julia/Desktop"
dirPath = "M:\Desktop\Studier\H12"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup"
#dirPath = os.getcwd()
digLvMax = 3 # How far into folders to dig. (0 => no max lv)
minSize = 50 #size (in Mb) to show. (0 => no min size)
showFiles = (1==1) # show files (if larger than minSize).
############################


## Good settings:
#dirPath = "C:/"
#digLvMax = 4 # How far into folders to dig. (0 => no max lv)
#minSize = 1000 #size (in Mb) to show. (0 => no min size)
#showFiles = (1==0) # show files (if larger than minSize).



## PC
#dirPath = "C:/"
#dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup"

## Android
#dirPath = 'storage/sdcard0' 

f=open("out.txt",'w')


def pf(subNR, size, name, path):
    tab="|"
    i=0
    while i<subNR:
        tab=tab+" -"
        i=i+1
    tab = tab+"|"
    if subNR==0:
        tab="*"
        
    GB=""
    if bToMb(size)>=1000:
        nr=Decimal(bToMb(size))/1024
        nr=round(nr,2)
        GB = "("+str(nr)+" Gb) "

    line = ""
    if digLvMax > subNR or digLvMax==0:
        if bToMb(size) >= minSize or minSize == 0:
            #print tab+" "+str(bToMb(size))+" "+name+" \n\t("+path+")"
            line = tab+" "+str(bToMb(size))+" Mb "+GB+"\""+name+"\""
    if len(line) > 0:
        print line
        f.write(line+"\n")


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
                BadOnes= BadOnes+"* "+item+" ("+directory+")\n"

    for folder in os.listdir(directory):
        if os.path.isdir(directory+"/"+folder):
            try:
                size = size + folderDigger(subNR, (directory+"/"+folder), folder)
            except:
                pass
    
    
    for fil in os.listdir(directory):
        if os.path.isfile(directory+"/"+fil):
            size = size+getsize(directory+"/"+fil)
            if showFiles:
                pf(subNR+1, getsize(directory+"/"+fil), fil, directory)
    
    
    pf(subNR, size, name, directory)
    return size
    
    
## "The Program"
folderDigger(-1, dirPath, dirPath)
print "\nBadOnes:"
print BadOnes


f.close()