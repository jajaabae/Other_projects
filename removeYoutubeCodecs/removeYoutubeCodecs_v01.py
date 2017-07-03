import os

path = 'storage/sdcard0'
os.chdir(path)
codecSpesificString = '...'

#itemlist=os.listdir(u''+str(path))
itemlist=os.listdir(os.getcwd())
resultListOfItems=[]
print os.path.isdir(path) 
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

