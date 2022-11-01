import cv2
import numpy as np

img = np.zeros((512,512))
img = np.zeros((512,512,3))

img[:] = 255,0,0

cv2.line(img,(0,0),(511,511),(0,255,0),3) #image_matrix, start point, end_point,color,line thickness
cv2.rectangle(img,(10,10),(250,350),(0,0,255),cv2.FILLED) #start, end, fill box or not / thickness
cv2.circle(img,(400,50),30,(255,10,10),5) #position radius
cv2.putText(img,"opencv_text",(480//2,511//2),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
# print(img)
cv2.imshow("img",img)
cv2.waitKey(0)
