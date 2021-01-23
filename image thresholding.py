import numpy as np
import cv2
import matplotlib.pyplot as plt

path="C:/Users/Asus/Desktop/imageProcessingOpenCV/imgs/"

img=cv2.imread(path+'img1.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold
_, thresh_image=cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY)

#adaptive threshold
thresh_image2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)


#cv2.imshow('img1',img)
plt.imshow(img,cmap='gray')
plt.axis('off')

plt.figure()
plt.imshow(thresh_image,cmap='gray')
plt.axis('off')

plt.figure()
plt.imshow(thresh_image2,cmap='gray')
plt.axis('off')

plt.show()


