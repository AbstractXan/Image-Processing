import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('testimage.jpg',cv2.IMREAD_COLOR)

#cv2.line(img,(0,0),(150,150), (255,255,255),15)
cv2.rectangle(img, (15,25),(948,631), (0,255,0), 5)
cv2.circle(img, (483,333) , 250, (0,0,255)) #-1 to fill

pts = np.array([[10,5],[20,30],[70,20],[50,10],[100,100]], np.int32)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2. putText(img, 'AMANDA CERNY <3', (500,130), font, 1, (200,255,255), 2 ,cv2.LINE_AA)
##plt.imshow(img,cmap='gray',interpolation='bicubic')
##plt.show()
cv2.polylines(img,[pts], True, (0,255,255),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
