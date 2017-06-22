import os
try:
    for item in os.listdir(os.getcwd()):
        if '.pyc' in item:
            #print item
            os.remove(item)
except:
    pass
