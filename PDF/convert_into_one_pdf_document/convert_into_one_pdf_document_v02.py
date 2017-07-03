from PIL import Image
from fpdf import FPDF
import os
#im = Image.open("Jaabaek_BSc_Chemistry (1).jpg")
#im.save("Jaabaek_BSc_Chemistry (1).pdf", "PDF", resolution=100.0)

"""
def conv(im_name):
    
    im = Image.open(im_name)
    out_im_name = im_name.replace(".jpg", ".pdf").replace(".JPG", ".pdf")
    im.save(out_im_name, "PDF", resolution=100.0)
"""

def get_path():
    f = open('path.txt', 'r')
    line = f.readline().replace('\n','').replace('\\','/')
    f.close()
    return line

#print get_path()

def main():
    os.chdir(get_path())
    
    image_ending = '.jpg'
    pdf = FPDF()

    h_im = 2338.
    w_im = 1700.
    ratio = h_im/w_im

    w = 215
    #w = 210
    h = w*ratio
    
    file_list = os.listdir(os.getcwd())
    file_list = sorted(file_list)
    out_name = ''
    for e in file_list:
        if image_ending in e.lower():
            pdf.add_page()
            if len(out_name)==0:
                out_name = e
            
            #pdf.set_font('Arial', '8', 16)
            #pdf.cell(40,10,'Hello World!')
            print e

            #im = Image.open(e)

            #pdf.image(im, 0, 0, 100, 100)
            #pdf.image(e, 0, 0, 100, 100)

            pdf.image(e,0,0,w,h)
            
            #conv(e)
    out_name = out_name.split('.')[0]+'.pdf'
    pdf.output(out_name, 'F')

main()
