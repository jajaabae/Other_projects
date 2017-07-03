import os #for example/test

class Settings():
    def __init__(s, path):
        s.settings_file_name = path+'/'+'settings.txt'
        s.read_settings()
        
    def read_settings(s):
        f = open(s.settings_file_name, 'r')
        settings_list = [l.replace('\n','').split('\t') for l in f.readlines()]
        f.close()
        
        for e in settings_list:
            var_name = e[0]
            var_value = e[1].replace('\\','/')
            exec_string = 's.'+var_name+' = "'+var_value+'"'
            exec(exec_string)

def example():
    #import os
    #from m.settings import Settings
    path = os.getcwd()
    settings = Settings(path)
    music_path = settings.music_path

if __name__ == '__main__':
    example()
