"""
def getPlaylistFromName_test(plName):
    tmp = {
        'TopZouk':[1, 2, 3],
        'ZoukFav':[4, 5, 6],
        'ZoukBra':[7, 8, 9],
        'Experimental':[2, 5, 8, 11],
        'ZoukOK':[10, 11, 12],
        }
    print plName
    return tmp[plName]


def getPlaylistFromName_true(plName):
    f = open('db/playlistsList.txt', 'r')
    lines = f.readlines()
    f.close()
    for l in lines:
        l = l.replace('\r','').replace('\n','')
        print l
    pl_dict = {'TopZouk':[1, 2, 3],}
    return pl_dict[plName]
"""

def getPlaylistCodeFromName(plName):
    f = open('db/playlistsList.txt', 'r')
    lines = f.readlines()
    f.close()
    pl_dict = {}
    for l in lines:
        l = l.replace('\r','').replace('\n','')
        #print l
        l = l.split('\t')
        #print l
        pl_dict[l[2]] = l[0]
    #pl_dict = {'TopZouk':[1, 2, 3],}
    result = None
    try:
        result = pl_dict[plName]
    except:
        pass
    return result


if __name__ == '__main__':
    print getPlaylistCodeFromName('TopZouk')
#    print getPlaylistFromName_true('TopZouk')
