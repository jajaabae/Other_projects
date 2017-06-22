def removeFilesInDir(path):
    import os
    liste=[]
    try:
        liste=os.listdir(path)
    except:
        pass
    for d in liste:
        if os.path.isfile(path+d):
            os.remove(path+d)
            print 'removed:', d
