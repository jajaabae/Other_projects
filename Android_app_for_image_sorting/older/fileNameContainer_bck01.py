import os
from gm.has_imageExtention import has_imageExtention

class fileNameContainer():
    count = 0
    images=[]
    
    def __init__(self):
        imgs = []
        for item in os.listdir(os.getcwd()):
            if has_imageExtention(item):
                imgs += [item]
        fileNameContainer.images=imgs
        
    def increment(self):
        if fileNameContainer.count == len(fileNameContainer.images)-1:
            fileNameContainer.count = 0
        else:
            fileNameContainer.count += 1
    def inv_increment(self):
        if fileNameContainer.count > 0:
            fileNameContainer.count -= 1
        else:
            fileNameContainer.count = len(fileNameContainer.images)-1
    
    def getCurrentFileName(self):
        ret = self.images[self.count]
        return ret
        
    def getNextFileName(self):
        self.increment()
        ret = self.images[self.count]
        return ret
        
    def getPrevFileName(self):
        self.inv_increment()
        ret = self.images[self.count]
        return ret
