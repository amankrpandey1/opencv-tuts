"to get bird eye view"
import numpy as np
import cv2
img = cv2.imread("./cards.jpg")
 
width,height = 250,350 #which we want 2.5:3.5 inches one card aspect ratio
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) #king of spade card location points
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #new corresponding points that you want that you want
matrix = cv2.getPerspectiveTransform(pts1,pts2) # define points cordinates from cordinates and to cordinates
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) # src image, matrix , and (h,w)
# print(matrix)
 
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
 
cv2.waitKey(0)
