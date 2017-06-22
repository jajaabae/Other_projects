def fromStr_nrX(l, X):
    l = l.replace('\n', '')
    l = l.split('\t')
    l = l[X-1]
    return l
