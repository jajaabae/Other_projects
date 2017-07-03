def f_getUniqueDataElements(data_from_lines):
    file_names = []
    dirs = []
    
    for l in data_from_lines:
        file_names += [l[0]]
        dirs += [l[2]]

    return file_names, dirs
