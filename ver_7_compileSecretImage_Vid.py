import glob

import cv2
import sys
import os
from numpy.random import randint
import numpy as np
frameSize=(1920,1080)

# replace the new encoded image frame with original frame
os.remove("C:/Users/Dell/PycharmProjects/Steganography_Vid/data/frame352.jpg")
os.rename('C:/Users/Dell/PycharmProjects/Steganography_Vid/data/encoded.jpg','C:/Users/Dell/PycharmProjects/Steganography_Vid/data/frame352.jpg')

out=cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'),29.97,frameSize)
for filename in glob.glob('C:/Users/Dell/PycharmProjects/Steganography_Vid/data/*jpg'):
    img=cv2.imread(filename)
    out.write(img)

out.release()
