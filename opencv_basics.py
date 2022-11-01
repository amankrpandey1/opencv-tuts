"""
1. reading images
2. display images
3. blur images
4. convert to grayscale images
5. edge detection
6. increasing and decreasing detected edge width
7.resizing the image
8. croppping imges
"""

import cv2
import numpy as np

img = cv2.imread("./img1.jpg") #reading image

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #comvert to grayscale

img_blur = cv2.GaussianBlur(img_gray,(3,3),1) #blur function

img_canny = cv2.Canny(img_blur,100,100) #edge detection

kernel = np.ones((3,3),np.uint8)  #kernel for increase the edge width

img_dilate = cv2.dilate(img_canny,kernel,iterations=1) #increase edge width

img_erode = cv2.erode(img_dilate,kernel,iterations=1) #decrease edge width

print(img.shape) #(height,width,channels) image dimensions
img_resize = cv2.resize(img,(400,325)) #resizing the image using function

img_cropped = img_resize[0:200,200:] #height width image cropping using numpy array

cv2.imshow("orignal",img) #image display
cv2.imshow("grayscale",img_gray) 
cv2.imshow("Blur",img_blur)
cv2.imshow("Canny",img_canny)
cv2.imshow("Dilated img",img_dilate)
cv2.imshow("Eroded img",img_erode)
cv2.imshow("resized img",img_resize) 
cv2.imshow("cropped img",img_cropped)

cv2.waitKey(0)
