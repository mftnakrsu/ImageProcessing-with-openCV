import cv2
import numpy as np



path="C:/Users/Asus/Desktop/imageProcessingOpenCV/lenna.png"
img=cv2.imread(path)

#horizontal
hor=np.hstack((img,img))
cv2.imshow('horizontal',hor)

#vertical
ver=np.vstack((img,img))
cv2.imshow('vertical',ver)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()