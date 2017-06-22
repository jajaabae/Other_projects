#import Image

import PIL
from PIL import Image
import os

import PIL
from PIL import Image

def resize_image(image, out_image_name):
    basewidth = 2000
    basewidth = 1000
    img = Image.open(image)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(out_image_name) 

def get_image_list(file_ending, exclude_string):
    items = os.listdir(os.getcwd())
    image_list = []
    for item in items:
        if item.split('.')[-1] == file_ending:
            if not exclude_string in item:
                image_list.append(item)
    return image_list



def main():
    file_ending = 'jpg'
    exclude_string = '_resized'
    image_list = get_image_list(file_ending, exclude_string)
    completed = os.listdir(os.getcwd()+'/'+'resized')
    #print image_list
    #print completed
    for image in image_list:
        out_image_name = image+'_resized.jpg'
        if out_image_name not in completed:
            out_image_name_in_path = 'resized'+'/'+out_image_name
            print out_image_name_in_path 
            resize_image(image, out_image_name_in_path)


main()
