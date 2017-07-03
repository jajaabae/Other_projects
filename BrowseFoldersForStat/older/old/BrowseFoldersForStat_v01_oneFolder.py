import os
from os.path import join, getsize, isfile, isdir, splitext

dirPath = "C:/"
dirPath = "C:/Users/Atrakatz/Google Drive/ContinousBackup/programming/python"

os.chdir(dirPath)
print os.getcwd()



TotalSize = 0
for item in os.walk(dirPath):
    for file in item[2]:
        try:
            TotalSize = TotalSize + getsize(join(item[0], file))
        except:
            print("error with file:  " + join(item[0], file))

#print str(TotalSize)+" b"
#print str(TotalSize/1024)+" kb"
print str(TotalSize/1024/1024)+" Mb"
print str(TotalSize /1024 /1024 /1024)+" Gb"
