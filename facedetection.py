import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
video=cv2.VideoCapture(0)

while True:
	bol,img=video.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray=cv2.GaussianBlur(gray,(21,21),0)
	faces=face_cascade.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
		roi_gray=gray[y:y+h,x:x+w]
		roi_Color=img[y:y+h,x:x+w]
		eyes=eye_cascade.detectMultiScale(roi_gray,1.6,3)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_Color,(ex,ey),(ex+ew,ey+eh),(0,255,5),3)
	cv2.imshow('img',img)
	key=cv2.waitKey(2)
	if key==ord('q'):
		break
video.release()		
cv2.destroyAllWindows()
	


