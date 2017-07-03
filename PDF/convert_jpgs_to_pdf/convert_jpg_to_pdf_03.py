from PIL import Image
import os
#im = Image.open("Jaabaek_BSc_Chemistry (1).jpg")
#im.save("Jaabaek_BSc_Chemistry (1).pdf", "PDF", resolution=100.0)


def conv(im_name):
    
    im = Image.open(im_name)
    out_im_name = im_name.replace(".jpg", ".pdf").replace(".JPG", ".pdf")
    im.save(out_im_name, "PDF", resolution=100.0)


def main():
    os.chdir(get_path())
    image_ending = '.jpg'
    #image_ending = '.bmp'
    for e in os.listdir(os.getcwd()):
        
        if image_ending in e.lower():
            print e
            conv(e)

def get_path():
    f = open('path.txt', 'r')
    line = f.readline().replace('\n','').replace('\\','/')
    f.close()
    return line


main()
