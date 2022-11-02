import cv2

faceCascade= cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml") #detect face of persion using haar cascade method
img = cv2.imread('./img1.jpg') 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
faces = faceCascade.detectMultiScale(imgGray,1.1,4) #detecting faces in the image
 
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #bounding box around faces
 
 
cv2.imshow("Result", img)
cv2.waitKey(0)
