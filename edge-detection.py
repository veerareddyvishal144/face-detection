import cv2
video=cv2.VideoCapture(0)
while True:
	bol,img=video.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray=cv2.bitwise_not(gray)
	#cv2.adaptiveThreshold
	cv2.imshow('neg-img',gray)
	edges=cv2.Canny(img,100,100)
	cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
	#cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
	cv2.imshow("window",edges)
	key=cv2.waitKey(2)
	if key==ord('q'):
		
		break
video.release()		
cv2.destroyAllWindows()
     



