def has_imageExtention(fileName):
    hasExtention = False
    #imageExtentions = ['.bmp', '.jpg', '.JPEG', '.png']
    imageExtentions = ['bmp', 'jpg', 'JPEG', 'png']
    for ie in imageExtentions:
        #print ie.lower(), fileName.lower()
        ext = fileName.split('.')[-1]
        #print ext
        if ie.lower() == ext.lower():
            #print ie.lower(), fileName.lower()
            hasExtention = True
    return hasExtention


#print has_imageExtention("something.txt.jpg")


"""
def has_imageExtention(fileName):
    hasExtention = False
    imageExtentions = ['.bmp', '.jpg', '.JPEG', '.png']
    for ie in imageExtentions:
        #print ie.lower(), fileName.lower()
        if ie.lower() in fileName.lower():
            #print ie.lower(), fileName.lower()
            hasExtention = True
    return hasExtention
#"""