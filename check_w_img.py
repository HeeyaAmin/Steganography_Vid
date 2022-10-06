import numpy as np
import cv2 as cv
from PIL import Image
from numpy import binary_repr

def img_pix():
    img = Image.open("kiwi.jpg")
    pixels = img.load() # this is not a list, nor is it list()'able
    width, height = img.size
    all_img_pixels = []
    for m in range(width):
        for n in range(height):
            cpixel = pixels[m, n]
            all_img_pixels.append(cpixel)

    for m in range(width):
        for n in range(3):
            z=np.binary_repr(all_img_pixels[m][n], width=8)
            imgpix=z[5:]
            print(imgpix)

img_pix()
