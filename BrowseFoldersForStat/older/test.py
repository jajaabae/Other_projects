import os
from os.path import join, getsize, isfile, isdir, splitext
from decimal import Decimal

dirPath = "C:/"
directory = dirPath


for folder in os.listdir(directory):
    print folder
    print "- "+str(getsize(directory+"/"+folder))
    if os.path.isdir(directory+"/"+folder):
        print "- Folder"
    else:
        print "- Not Folder"

