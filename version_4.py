import cv2
import numpy
import os
from PIL import Image
from subprocess import call,STDOUT  #FFmpeg is a free and open-source command-line tool for transcoding multimedia files. It contains a set of shared audio and video libraries such as libavcodec, libavformat, and libavutil. With FFmpeg, you can extract audio files from a video, convert your PNG image files into video, and much more.
vid = cv2.VideoCapture("video.mp4") #video input liya

if (vid.isOpened()==False): #agar file nahi open hui tohh
    print("Couldn't open video")
else:
    F = vid.get(cv2.CAP_PROP_FRAME_COUNT)  #frames total
    x = vid.get(cv2.CAP_PROP_FPS)          #fps count
    print("total number of frames ", F)
    print("frames per second ", x)


#code to break the video into respective frames
# try:
#     if not os.path.exists('data'):
#         os.makedirs('data')
# except OSError:
#     print("Error creating directory of data")
#
# #frame
# currentFrame=0
#
# while(True):
#     ret,frame = vid.read()
#
#     if ret:
#         name = './data/frame'+str(currentFrame) + '.jpg'
#         print('Creating...'+name)
#
#         cv2.imwrite(name,frame)
#
#         currentFrame+=1
#     else:
#         break
#
# vid.release()
# cv2.destroyAllWindows()


# take input of image to be hidden
img = Image.open("kiwi.jpg")
pixels = img.load() # this is not a list, nor is it list()'able
width, height = img.size
all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        # print(cpixel)
        all_pixels.append(cpixel)


# next to be done
# msb of kiwi add to lsb of any frame


# code to hide apple.jpg in a frame
