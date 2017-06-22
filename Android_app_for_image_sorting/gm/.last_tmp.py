def get_btnList():
    abtnList = ['B', 'C', 'D']
    abtnList = ['B', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D']
    abtnList = ['B', 'C', 'D', 'C', 'D', 'C', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D', 'C', 'D']
    abtnList = list('qwertyuioplkjhgfdsazxcvbnmMNBVCXZLKJHGFDSAQWERTYUIOP')
    abtnList = ['Notes',
                'Experience',
                'Art',
                ]
    
    abtnList = ['Notes',
                'Experience',
                'Art',
                'bad',
                'annet',
                ]
    
    return abtnList


if __name__ == '__main__':
    print type(get_btnList())
    print get_btnList()