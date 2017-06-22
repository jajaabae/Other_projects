#-*-coding:utf8;-*-
#qpy:2
#qpy:console


def emptyLog():
    pass
def addLineToFile():
    pass
def reduceFileToUniqueLines():
    pass 
def logger(errortype, errorMsg):
    f=open('db/log/'+errortype,'w')
    f.write('x\n') 
    f.close()
    
    f=open('db/log/'+errortype+'.txt','r')
    lines = f.readlines()
    lines += errorMsg+'\n'
    f.close()
    
    lines = ''.join(lines)
    print lines
    f=open('db/log/'+errortype,'w')
    f.write(lines)
    f.close()