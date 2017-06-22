from bs4 import BeautifulSoup
import platform

def osbs(webPage):
    bs=''
    if platform.system() == 'Linux':
        bs=BeautifulSoup(webPage)
    else:
        bs=BeautifulSoup(webPage, "lxml")
    return bs
