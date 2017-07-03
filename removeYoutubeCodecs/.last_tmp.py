import os

path = 'storage/sdcard0'
os.chdir(path)
codecSpesificString = 'ACodec.OMX.'

print os.getcwd()

#itemlist=os.listdir(u''+str(path))
itemlist=os.listdir(os.getcwd())
resultListOfItems=[]
print os.path.isdir(path) 

def program():
    for item in itemlist:
        print 'Checking: '+item
        print path+'/'+item
        #if os.path.isfile(path+'\\'+item):
        #if os.path.isfile(path+'/'+item):
        print os.path.isdir(path+'/'+item)
        if os.path.isdir(path+'/'+item):
            print 'is file: '+item
            if codecSpesificString in item:
                print '-Removing: '+item

def testPathForFiles(path):
    liste=[]
    print ' test'
    try:
        #liste=os.listdir(path)
        path = os.getcwd() 
        liste=os.listdir(os.getcwd())
    except:
        print  'fail' 
        pass
    for d in liste:
        print ''
        dpath= (path+'/'+d)
        if os.path.isdir(dpath):
            print 'isdir: '+dpath
        elif os.path.isfile(dpath):
            #handleMusicFile(d,path,dpath)
            print 'isfile: '+dpath
            if codecSpesificString in d:
                print '-Removing: '+d
                os.remove(dpath)

testPathForFiles(path)
#program()