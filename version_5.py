import cv2
from subprocess import call,STDOUT
import os
vidcap = cv2.VideoCapture("video.mp4")
success, image = vidcap.read()
count=0
while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1

        
def encode_string(input_string,root="./tmp/"):
    split_string_list=split_string(input_string)
    for i in range(0,len(split_string_list)):
        f_name="{}frame{}.jpg".format(root,i)
        secret_enc=lsb.hide(f_name,split_string_list[i])
        secret_enc.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name,split_string_list[i]))


call(["ffmpeg", "-i", "tmp/frame%d.png" , "-vcodec", "png", "video.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)