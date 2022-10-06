#to extract frames from video
import cv2
import sys
import numpy as np
import os
import datetime
from stegano import lsb

# video steganography mai pehle break into frames
# this code below is for image to image steganography
# secret=lsb.hide ('apple.jpg','kiwi.jpg')

# video input
vidcap = cv2.VideoCapture("video.mp4")

# image input
img1 = cv2.imread("apple.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("kiwi.jpg",cv2.IMREAD_COLOR)

# # displays images to be hidden
# cv2.imshow("First Image",img1)
# cv2.imshow("Secong Image",img2)
# # holds the images on screen
# cv2.waitKey(0)
# # destroys memory space ie free krega
# cv2.destroyAllWindows()

    # print("enter the ratio of used to unused frames")
    # c=input("unused frames")


# calculate total number of frames and fps
F = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
x = vidcap.get(cv2.CAP_PROP_FPS)
print("total number of frames ",F)
print("frames per second ",x)

# calculate duration of video
y = round(F/x)
print(f"duration of video in seconds: {y}")

# random number
D=int(input("Enter a random number"))
print(D)

# ratio of frames to be used for storing hidden info to be used to contain random data is b:c
b=int(input("enter number of frames to be used for storing hidden information "))
c=int(input("enter number of frames to be used for random data "))

# frames to be used for steganography u=(b/b+c)*F
u=(b/(b+c))*F
print(u)

# size of secret data
apple_size=(os.stat('apple.jpg').st_size)*8
kiwi_size=(os.stat('kiwi.jpg').st_size)*8
print("size of secret data ",(apple_size+kiwi_size))




# resolution of video mxn
m = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
n = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"resolution of video is {m} x {n}")

#
# #code from line 44 to 67 is to break the video into respective frames
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
#     ret,frame = vidcap.read()
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
# vidcap.release()
# cv2.destroyAllWindows()
#
#






# https://betterprogramming.pub/a-guide-to-video-steganography-using-python-4f010b32a5b7