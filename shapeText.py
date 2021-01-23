import cv2
import numpy as np

#create black image
img= np.zeros((512,512,3),np.uint8)
print(img.shape)

cv2.imshow('Black Image',img)

#line
#(img,sp,fp,colour,thickness)
cv2.line(img,(0,0),(512,512),(0,255,0),3)#opencv bgr
cv2.imshow('Green Image',img)

#rectangle
cv2.rectangle(img,(0,0),(256,139),(255,0,0),-1)#cv2.FILLED
cv2.imshow('Rectangle Image',img)

#circle
cv2.circle(img,(250,300),65,(0,0,255),-5)
cv2.imshow('Cırcle Image',img)

#text
cv2.putText(img,"Imagetext",(150,359),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,200),2)
cv2.imshow('Text Image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
