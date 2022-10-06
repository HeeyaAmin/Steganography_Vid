import numpy as np
import cv2 as cv
from numpy import binary_repr
from PIL import Image


# Function to convert decimal to binary
# using built-in python function
# def decimalToBinary(n):
#     # converting decimal to binary
#     # and removing the prefix(0b)
#     return bin(n).replace("0b", "")

# def messageToBinary(message):
#     if type(message) == str:
#         return ''.join([ format(ord(i), "08b") for i in message ])
#     elif type(message) == bytes or type(message) == np.ndarray:
#         return [ format(i, "08b") for i in message ]
#     elif type(message) == int or type(message) == np.uint8:
#         return format(message, "08b")
#     else:
#         raise TypeError("Input type not supported")



# if __name__=='__main__':




count=0

vidcap = cv.VideoCapture("video.mp4")
if not vidcap.isOpened():
    print("Cannot open")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = vidcap.read()
     # -------------------------------------------------------------> step 2 - split
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', gray)
    width, height, d= frame.shape
    print("reshaped...")
    row=int(width*height)
    newframe = frame.reshape(row,3) #2D mein change kiya
    newframe_list=newframe.tolist()
    # print(type(newframe_list))
    all_pixels=[] #empty list
    # print(newframe_list)
    for i in newframe_list:
        all_pixels.extend(i)

        for i in all_pixels:
            x=np.binary_repr(all_pixels[i], width=8)
            vidpix=x[5:]
            print(x)

    print("image pixels")
    #kiwi wali image ke pixels iterate kr rhe
    def img_pix():
        img = Image.open("kiwi.jpg")
        pixels = img.load()  # this is not a list, nor is it list()'able
        w, h = img.size
        all_img_pixels = []
        for m in range(w):
            for n in range(h):
                cpixel = pixels[m, n]
                all_img_pixels.append(cpixel)

        for m in range(w):
            for n in range(3):
                z = np.binary_repr(all_img_pixels[m][n], width=8)
                imgpix = z[6:]
                print(z)


    img_pix()

    # for x in newframe_list:
    #     for y in x:
    #         all_pixels.append(y)
    #         print(all_pixels)


    # for i in range(row):
    #     for j in range(3):
    #         cpixel = newframe_list[i, j]
    #         all_pixels.append(cpixel)
    #
    # for i in range(row):
    #     for j in range(3):
    #         print(all_pixels[i][j])

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture

vidcap.release()
cv.destroyAllWindows()








