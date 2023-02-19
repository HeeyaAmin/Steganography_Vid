# Importing all necessary libraries
import cv2
import sys
import os
from numpy.random import randint
import numpy as np

import glob
from PIL import Image
MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8
##############################################################################################################################
def make_image(data, resolution):
    image = Image.new("RGB", resolution)
    image.putdata(data)
    return image


def remove_n_least_significant_bits(value,n):
    value = value >> n
    return value << n

def get_n_least_significant_bits(value, n):
    value = value << MAX_BIT_VALUE - n
    value = value % MAX_COLOR_VALUE
    return value >> MAX_BIT_VALUE - n

def get_n_most_significant_bits(value, n):
    return value >> MAX_BIT_VALUE - n

def shit_n_bits_to_8(value, n):
    return value << MAX_BIT_VALUE - n


def encode(image_to_hide, image_to_hide_in, n_bits):

    width, height = image_to_hide.size

    hide_image = image_to_hide.load()
    hide_in_image = image_to_hide_in.load()

    data = []

    for y in range(height):
        for x in range(width):

            # (107, 3, 10)
            # most sig bits
            r_hide, g_hide, b_hide = hide_image[x,y]

            r_hide = get_n_most_significant_bits(r_hide, n_bits)
            g_hide = get_n_most_significant_bits(g_hide, n_bits)
            b_hide = get_n_most_significant_bits(b_hide, n_bits)

            # remove lest n sig bits
            r_hide_in, g_hide_in, b_hide_in = hide_in_image[x,y]

            r_hide_in = remove_n_least_significant_bits(r_hide_in, n_bits)
            g_hide_in = remove_n_least_significant_bits(g_hide_in, n_bits)
            b_hide_in = remove_n_least_significant_bits(b_hide_in, n_bits)

            data.append((r_hide + r_hide_in,
                         g_hide + g_hide_in,
                         b_hide + b_hide_in))

    return make_image(data, image_to_hide.size)


def decode(image_to_decode, n_bits):
    width, height = image_to_decode.size
    encoded_image = image_to_decode.load()

    data = []

    for y in range(height):
        for x in range(width):
            r_encoded, g_encoded, b_encoded = encoded_image[x, y]

            r_encoded = get_n_least_significant_bits(r_encoded, n_bits)
            g_encoded = get_n_least_significant_bits(g_encoded, n_bits)
            b_encoded = get_n_least_significant_bits(b_encoded, n_bits)

            r_encoded = shit_n_bits_to_8(r_encoded, n_bits)
            g_encoded = shit_n_bits_to_8(g_encoded, n_bits)
            b_encoded = shit_n_bits_to_8(b_encoded, n_bits)

            data.append((r_encoded, g_encoded, b_encoded))

    return make_image(data, image_to_decode.size)

if "__main__":

    ##############################################################################################################################

    # Read the video from specified path
    cam = cv2.VideoCapture("output_video.avi")

    try:
        # creating a folder named data
        if not os.path.exists('dataDecr'):
            os.makedirs('dataDecr')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0

    while (True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = './dataDecr/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

    #########################################################################################################################

    # generate random integer to select a random frame
    # generate some integers
    # values = int(randint(0, currentframe, 1))
    # print(values)
    # em_img = './dataDecr/frame' + str(values) + '.jpg'
    # name_sel_img='frame'+str(values)
    # print(name_sel_img)
    # selected_img_read = cv2.imread(em_img, cv2.IMREAD_ANYCOLOR)




    # # to show the selected frame
    # while True:
    #     cv2.imshow("select_frame", img)
    #     cv2.waitKey(0)
    #     sys.exit()  # to exit from all the processes
    #
    # cv2.destroyAllWindows()  # destroy all windows

    ########################################################################################################################

    image_to_hide_path = "./sunflower.jpg"
    # image_to_hide_in_path = em_img
    encoded_image_path = "./data/frame352.jpg"
    decoded_image_path = "./decoded.jpg"
    n_bits = 2
    values=352

    # image_to_hide = Image.open(image_to_hide_path)
    # image_to_hide_in = Image.open(image_to_hide_in_path)

    for i in range(0,values+1):
        while i==values:
            # encode(image_to_hide, image_to_hide_in, n_bits).save(encoded_image_path)

            image_to_decode = Image.open(encoded_image_path)
            decode(image_to_decode, n_bits).save(decoded_image_path)
            break


    #######################################################################################################
    # vid decrypt krne wala rough code

    # os.remove(em_img)
    # print("removed image %s"%em_img)
    #
    # image_folder = 'data'
    # video_file = 'compiled_vid.mp4'
    # image_size = (1920, 1080)
    # fps = 30
    #
    # images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    # images.sort()
    # fourcc = 0x7634706d
    # out = cv2.VideoWriter(video_file, fourcc, fps, image_size)
    #
    # img_array = []
    # for filename in images:
    #     img = cv2.imread(os.path.join(image_folder, filename))
    #     img_array.append(img)
    #     out.write(img)
    #
    # out.release()


