#Set-up

import os
import matplotlib.pyplot as plt 
import cv2 as cv
import segmentation_functions
import segmentation_functions

#Change directory to image dir.
dir_images="/home/abraham/Escritorio/PAE2/PAE/pae2019/CLOCK/CDT_images"
os.chdir(dir_images)

#Image names

images=os.listdir()
image=images[0]

#Preprocessing

##Read image in RGB space
img=cv.imread(images[0],cv.IMREAD_color)
## RGB image to gray scale
gray=cv.cvtColor(img.cv.COLOR_BGR2GRAY)
##Binarize image
ret,tresh=cv.threshold(gray,127,255,0)

#Detect contours

contours,hierarchy=cv2.findContours(thresh,cv.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Draw contorus

segmentation_functions.draw_object_detection(image,contours)
