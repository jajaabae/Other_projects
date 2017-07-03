def f_getDirTag(a_dir):
    dir_tag = a_dir.replace('\\', '').replace('/', '').replace(' ','').replace('_','').replace('\n','').replace(':','')
    return dir_tag
