##Color Detection using Python

import numpy as np
import cv2
from image_stacking import stackImages #available in same repo

def empty(a):
    pass


# creating a trackbar window to play with hsv value to detect a particular color

cv2.namedWindow("trackbar") #new window named trackbar
cv2.resizeWindow("trackbar",640,240) #size of trackbar windows
cv2.createTrackbar("Hue_min","trackbar",0,179,empty) #"trackbar name, window name, default value, max value, rec fun"
cv2.createTrackbar("Hue_max","trackbar",12,255,empty)
cv2.createTrackbar("Sat_min","trackbar",49,179,empty)
cv2.createTrackbar("Sat_max","trackbar",253,255,empty)
cv2.createTrackbar("Val_min","trackbar",178,179,empty)
cv2.createTrackbar("Val_max","trackbar",253,255,empty)

while True: #iterating loop to see live updation
    img = cv2.imread("./img1.jpg") #reading image
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #convert image to hsv format hue saturation value

    h_min = cv2.getTrackbarPos("Hue_min","trackbar") #get  pos value of Hue_min trackbar
    h_max = cv2.getTrackbarPos("Hue_max","trackbar")
    val_min = cv2.getTrackbarPos("Val_min","trackbar")
    val_max = cv2.getTrackbarPos("Val_max","trackbar")
    sat_min = cv2.getTrackbarPos("Sat_min","trackbar")
    sat_max = cv2.getTrackbarPos("Sat_max","trackbar")

    print(h_min,h_max,sat_min,sat_max,val_min,val_max) #printing the above values to see real time update

    lower = np.array([h_min,sat_min,val_min])  # creating array of min value of h s and v
    upper = np.array([h_max,sat_max,val_max]) # creating array of max value of h s and v
    mask = cv2.inRange(img_hsv,lower,upper) # creating a mask using upper and lower value white portion is detected color and black portion is neglected colors(1/0)
    img_result = cv2.bitwise_and(img,img_hsv,mask=mask)  #showing colors correspoding to masked array values only 1's(white portion) color will be shown in image
    # cv2.imshow("orig_image",img)
    # cv2.imshow("HSV_image",img_hsv)
    # cv2.imshow("mask_image",img_results)
    # cv2.waitKey(1)

    imgStack = stackImages(1,([img,img_hsv],[mask,img_result]))

    cv2.imshow("Stacked Images", imgStack)
    cv2.waitKey(1)
    
    # ctrl+z to exit
    # 0 12 49 255 179 255 skin color 
    #0 255 0 116 0 92  black color
