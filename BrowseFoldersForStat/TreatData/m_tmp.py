def rni(fn):
    s = '''
global %s
import %s
reload(%s)
from %s import %s
'''
    s = s%(fn, fn, fn, fn, fn)
    exec(s)

rni('f_readDataFromFile')
rni('f_readDataFromFile')
rni('f_getUniqueDataElements')
rni('f_getListOfUniqueItems')
rni('f_getDirsWithFiles')
rni('f_getFilesWithDirs')


def m_tmp():
    file_name = 'BFFS_out_data.txt'
    data_from_lines = f_readDataFromFile(file_name)
    [file_names, dirs] = f_getUniqueDataElements(data_from_lines)
    #print len(dirs)
    unique_dirs = f_getListOfUniqueItems(dirs)
    #print len(unique_dirs)

    dirs_with_files = f_getDirsWithFiles(unique_dirs, data_from_lines)
    #for l in dirs_with_files:
    #    print 
    #    print l.el[0], l.el[1]

    files_with_dirs = f_getFilesWithDirs(data_from_lines)
    for l in files_with_dirs:
        print 
        print l.el[0], len(l.el[1])


if __name__ == '__main__':
    m_tmp()










