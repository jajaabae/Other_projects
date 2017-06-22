def FolderDigger(path):
    import os
    filListe = []
    
    liste=[]
    maxDepth = 100
    try:
        liste=os.listdir(path)
    except:
        pass
    for d in liste:
        dpath= (path+'/'+d)
        if os.path.isdir(dpath):
            if len(liste)>0:
                p= (path+'/'+d)
                filListe += FolderDigger(p)
        elif os.path.isfile(dpath):
            #print d
            filListe += [dpath]
    return filListe
