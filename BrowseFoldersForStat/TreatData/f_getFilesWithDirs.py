def rni(fn):
    s = '''
global %s
import %s
reload(%s)
from %s import %s
'''
    s = s%(fn, fn, fn, fn, fn)
    exec(s)

rni('f_getDirFromDataLine')
rni('f_getFileNameFromDataLine')

class AnElement():
    pass

def f_getFilesWithDirs(data_from_lines):
    dirs_with_files = []
    for d in data_from_lines:
        a_dir = f_getDirFromDataLine(d)
        a_file_name = f_getFileNameFromDataLine(d)

        bool_need_new_spot = True
        for e in dirs_with_files:
            #print '*', e[0], a_dir, '***' #, a_dir
            if e.el[0] == a_file_name:
                #print a_dir
                bool_need_new_spot = False
                #print e
                
                e.el = [e.el[0] , e.el[1]+[a_dir]]
                #print e
                #dirs_with_files += [e]
                #print dirs_with_files
        if bool_need_new_spot:
            #print a_dir
            new_e = AnElement()
            new_e.el = [a_file_name, [a_dir]]
            #print 'new_e', new_e
            dirs_with_files += [new_e]
        
    #print
    #print 
    #for l in dirs_with_files:
    #    print 
    #    print l.el[0], l.el[1]
    
    
    return dirs_with_files
