#Contour/Shape detection
"""
Stpes:
1.load image and convert it into grayscale
2.blur to get the better edges
3.using canny edge detection get the edges
4. create function for getting countours
5. 
"""

import numpy as np
import cv2
from image_stacking import stackImages

def get_cotours(img,gauss_kernel = (7,7),canny_thres1 = 50,canny_thres2 = 50):
    """
    this function will detect the shapes which are present in your image and will show the names of the shapes on the picture
    params:
    1. img_canny : orig img matrix
    2. gauss_kernel : kernel size for gaussian filter(7,7)
    3. canny_thres1: 50
    4. canny_thres2: 50
    """
    img_for_contour = img.copy()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray,gauss_kernel,1)
    img_canny = cv2.Canny(img_blur,canny_thres1,canny_thres2)
    coutours, hierarchy = cv2.findContours(img_canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #image, external edges and assumes it is closed shape, all the shapes that are present
    for cnt in coutours:
        area = cv2.contourArea(cnt) #find the area of that perticular contour
        # print(area)
        if area>500:
            cv2.drawContours(img_for_contour,cnt,-1,(0,0,255)) #image on which you have to draw the shape, shape, id -1 for all the found shapes
            peri = cv2.arcLength(cnt,True) #method to find perimeter shape, closed or not
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #gives the total edges int the shape in simple words
            # print(len(approx))
            obj_cor = len(approx)
            x,y,w,h = cv2.boundingRect(approx) # used for bounding box the shape detected

            if obj_cor==3: 
                object_type = 'Tri'
            elif obj_cor==4:
                asp_ratio = w/float(h) # if close to 1 then it is a square else rect because in square,height=width
                if asp_ratio>0.98 and asp_ratio<1.03:
                    object_type = 'Square'
                else:
                    object_type = "Rect"
            elif obj_cor>4:
                object_type = "Cir"
            else:
                object_type = "None"
            cv2.rectangle(img_for_contour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img_for_contour,
                        object_type,
                        (x+(w//2)-30,y+(h//2)),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.7,
                        (0,0,0),2) 
    return img_for_contour

img = cv2.imread("./shapes.png")
img_for_contour = get_cotours(img)


stacked_img = stackImages(0.8, ([img,img_for_contour],
                            ))
cv2.imshow("stacked",stacked_img)
cv2.waitKey(0)
