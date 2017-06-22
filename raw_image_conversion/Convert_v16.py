import rawpy
import imageio
import os
import time

def get_files_in_dir(base_dir = None):
    if base_dir == None:
        base_dir = os.getcwd()
    files_in_dir = []
    for item in os.listdir(base_dir):
        #print item
        item_in_path = os.path.join(base_dir, item)
        if os.path.isfile(item_in_path):
            files_in_dir.append(item)
    return files_in_dir

def get_input_image_name_list(file_ending_list):
    #image_name_list = ["_MG_0754.CR2"]
    image_name_list = []
    files_in_dir = get_files_in_dir(base_dir = None)
    for file_name in files_in_dir:
        #print file_name
        for file_ending in file_ending_list:
            #if file_ending.lower() in file_name.lower():
            if file_ending.lower() == file_name[-len(file_ending):].lower():
                image_name_list.append(file_name)
    return image_name_list, files_in_dir

def read_image(image_name):
    raw = rawpy.imread(image_name)
    return raw

def process_image(raw):
    #rgb = raw.postprocess()
    rgb = raw.postprocess(
                          #output_color=rawpy.ColorSpace.raw,
                          #gamma=(1, 1),
                          use_camera_wb=True,
                          output_bps=16,
                          #user_wb=extrMult,
                          no_auto_bright=True,
                          #bright=extrBright,
                          bright=2,
                          #demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD
                          )
    return rgb

def get_out_name(image_name):
    #out_name = image_name.split('.')
    #out_name = out_name[0]+".jpg"
    out_name = image_name+".jpg"
    return out_name

def write_image(rgb, out_name):
    imageio.imsave(out_name, rgb)



def iterate_over_images(image_name_list, files_in_dir):
    tot_raw_images = len(image_name_list)
    non_converted_image_name_list = [image_name for image_name in image_name_list if get_out_name(image_name) not in files_in_dir]
    image_name_list = non_converted_image_name_list
    count = 0.
    #count = 10.
    tot_non_converted = len(image_name_list)
    #prcnt = int(count/tot*100)
    #print "{}%".format(prcnt)
    time_start = time.clock()

    #"""
    for image_name in image_name_list:
        images_left_of_none_converted = tot_non_converted-count
        tot_count = (tot_raw_images-tot_non_converted) + count
        prcnt = int(float(tot_count)/tot_raw_images*100)
        #print tot_raw_images, count, images_left_of_none_converted, tot_count
        spent_time = time.clock() - time_start
        try:
            time_left = (images_left_of_none_converted) * spent_time/count
            time_left_sec = int(time_left)
            time_left_min = int(time_left/60)
        except:
            time_left_sec = '-'
            time_left_min = '-'
        print "{}% {}/{} {}min or {}s".format(prcnt, int(tot_count), tot_raw_images, time_left_min, time_left_sec), image_name,
        count+=1
        out_name = get_out_name(image_name)
        if out_name in files_in_dir:
            pass
            print 'skiped'
        else:
            raw = read_image(image_name)
            rgb = process_image(raw)
            write_image(rgb, out_name)
            print ''
    #"""
        

def main():
    #file_ending = '.CR2'
    file_ending_list = ['.CR2', '.ARW', '.NEF']
    image_name_list, files_in_dir = get_input_image_name_list(file_ending_list)
    iterate_over_images(image_name_list, files_in_dir)
    #iterate_over_images_tmp(image_name_list)#ARW
    #iterate_over_images_tmp2(image_name_list)#tmp


#############################################
def iterate_over_images_tmp(image_name_list):
    for image_name in image_name_list:
        print image_name
        raw = read_image(image_name)
        rgb = process_image_tmp(raw)
        out_name = get_out_name(image_name)
        write_image(rgb, out_name.replace('.', '.'))
        
def process_image_tmp(raw):
    #rgb = raw.postprocess()
    rgb = raw.postprocess(
                          #output_color=rawpy.ColorSpace.raw,
                          #gamma=(1, 1),
                          use_camera_wb=True,
                          output_bps=16,
                          #user_wb=extrMult,
                          no_auto_bright=True,
                          #bright=extrBright,
                          bright=2,
                          #demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD
                          )
    return rgb
#############################################
def iterate_over_images_tmp2(image_name_list):
    for image_name in image_name_list:
        print image_name
        raw = read_image(image_name)
        rgb = process_image_tmp2(raw)
        out_name = get_out_name(image_name)
        write_image(rgb, out_name.replace('.', '_tmp4.'))
        
def process_image_tmp2(raw):
    #rgb = raw.postprocess()
    rgb = raw.postprocess(
                          #output_color=rawpy.ColorSpace.raw,
                          gamma=(2, 2),
                          use_camera_wb=True,
                          #output_bps=16,
                          #user_wb=extrMult,
                          no_auto_bright=True,
                          #bright=extrBright,
                          bright=5,
                          #demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD
                          )
    return rgb
#############################################


main()
