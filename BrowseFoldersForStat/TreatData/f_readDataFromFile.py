def f_readDataFromFile(file_name):
    data_from_lines = []
    f = open(file_name, 'r')
    for l in f:
        data_from_lines += [l.split('\t')]
    f.close()
    return data_from_lines

if __name__ == '__main__':
    file_name = 'BFFS_out_data.txt'
    data_from_lines = f_readDataFromFile(file_name)
    for l in data_from_lines:
        print l
