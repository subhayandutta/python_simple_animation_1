# VERY IMPORTANT
# Make sure you have the same file sizes or approximately the same for attaching the files together.
# For some reason this does not work if files of diff sizes are attempted to join to create a video.

import cv2
import os
from os.path import isfile, join
import sys, getopt

image_folder = ''
fps = 0

if len (sys.argv) < 3 :
    print ("Usage: python StichImages.py <input folder> <fps> <repeat (optional, defaults to 1)>")
    sys.exit (1)

count=0
repeat=1
for args in sys.argv:
    count=count+1
    if ( count == 2 ):
        image_folder = args
        if (not image_folder.endswith("/")):
            image_folder += "/"
    if ( count == 3 ):
        fps = args
    if ( count == 4 ):
        repeat = int(args)

if repeat == 0:
    repeat = 1

video_name = './video.mp4'

pathIn= image_folder
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f)) and ( f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg"))]

def last_3chars(x):
    return(int(x[-7:-4]))

files = sorted(files, key = last_3chars)

#natsort.natsorted(files,reverse=False)

frame_array = []
size=None
for i in range(repeat):
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        
        #inserting the frames into an image array
        frame_array.append(img)

out = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'DIVX'), int(fps), size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()

