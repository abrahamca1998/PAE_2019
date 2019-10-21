#Set-up

import os
import matplotlib.pyplot as plt 
import cv2 as cv
import segmentation_functions

#This function returns the indexes of the delimiter rectangle of each object detected.
def x_y_Contours(contours,contour):
    x=[]
    y=[]
    x=list(contours[contour].T[1])
    y=list(contours[contour].T[0])
    min_x=int(min(min(x)))
    max_x=int(max(max(x)))
    min_y=int(min(min(y)))
    max_y=int(max(max(y)))
    return x,y,min_x,max_x,min_y,max_y

#Draw rectangles in order to ease the visualitzation of segmentation.

def draw_object_detection(img,contours):
    for contour in range(len(contours)):
        (x_list,y_list,min_x,max_x,min_y,max_y)=x_y_Contours(contours,contour)
        print(type(int(min_x)))
        cv.rectangle(img,(min_y-10,min_x-10),(max_y+10,max_x+10),(255,0,0),2)
    plt.imshow(img)
    plt.show()
        