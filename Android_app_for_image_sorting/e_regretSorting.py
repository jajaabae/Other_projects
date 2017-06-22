#-*-coding:utf8;-*-
#qpy:2
#qpy:console

#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import os
import shutil

def regretSorting():
    p = os.path.realpath(__file__).replace('\\', '/').split('/')
    p = '/'.join(p[0:-1])
    os.chdir(p)
    
    cwd = os.getcwd()
    sortedRoot = cwd+'/'+'SORTED'
    for subFolder in os.listdir( sortedRoot ):
        if os.path.isdir( sortedRoot+'/'+ subFolder ):
            print subFolder
            for item in os.listdir( sortedRoot+'/'+subFolder ):
                itemInFolder = sortedRoot+'/'+subFolder+'/'+item
                if os.path.isfile( itemInFolder ):
                    print item
                    src = itemInFolder
                    dst = cwd+'/'+item
                    #print src, '\n', dst
                    shutil.move(src, dst)
    #deleteSortedFolder(sortedRoot)
            
def deleteSortedFolder( sortedRoot ):
    #os.remove(sortedRoot)
    shutil.rmtree(sortedRoot)

regretSorting()



"""
def sortFilesToFolders():
    p = os.path.realpath(__file__).replace('\\', '/').split('/')
    p = '/'.join(p[0:-1])
    os.chdir(p)
    
    for text in filesOfType('txt'):
        print
        for original in filesOfType(['png', 'jpg']):
            if original == text.replace('.txt', ''):
                print original, text
                tagComb = getTagCombination(text)
                
                tagNamedFolder = tagComb
                cwd = os.getcwd()
                moveToFolder(cwd, tagNamedFolder, [original, text])
                
def filesOfType(typeString):
    fileItemList = []
    if type(typeString) == type(''):
        for item in os.listdir(os.getcwd()):
            if os.path.isfile(item):
                if item.split('.')[-1] == typeString:
                    fileItemList += [item]
    elif type(typeString) == type([]):
        typeList = typeString
        for item in os.listdir(os.getcwd()):
            if os.path.isfile(item):
                for e in typeList:
                    if item.split('.')[-1] == e:
                        fileItemList += [item]    
    return fileItemList

def getTagCombination(fileName):
    f = open(fileName, 'r')
    lines =[] 
    for l in f:
        lines+=[l.replace('\n','')]
    f.close()
    lines = sorted(lines)
    s = '_'.join(lines)
    return s
    
def moveToFolder(cwd, tagNamedFolder, fileList):
    for item in fileList:
        print 'move', item
        src = cwd+'/'+ item
        dstFolder = cwd+'/' + 'SORTED/'+ tagNamedFolder
        dst = dstFolder+'/'+item
        #print src
        #print dst
        
        ##MakeDir if absent:
        if not os.path.exists( cwd+'/' + 'SORTED/' ):
            os.mkdir( cwd+'/' + 'SORTED/' )
        
        #print 'TEST1:', os.path.exists( dstFolder )
        if not os.path.exists( dstFolder ):
         #   print 'absent'
          #  print 'dstFolder:', dstFolder
            os.mkdir(dstFolder)
        else:
#            print 'OK'
            pass
        #print 'TEST2:', os.path.exists( dstFolder )
        
        ##move:
        shutil.move(src, dst)


sortFilesToFolders() 
#"""


