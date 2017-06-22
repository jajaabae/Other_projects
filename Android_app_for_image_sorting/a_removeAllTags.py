#-*-coding:utf8;-*-
#qpy:2
#qpy:console


def removeAllTags():
    import os
    p = os.path.realpath(__file__).replace('\\', '/').split('/')
    p = '/'.join(p[0:-1])
    os.chdir(p)
    
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(item):
            if item.split('.')[-1] == 'txt':
                print item
                os.remove(item)
    
removeAllTags()
