import cv2
import numpy as np
import matplotlib.pyplot as plt

path="C:/Users/Asus/Desktop/imageProcessingOpenCV/imgs/"

img1=cv2.imread(path+"img1.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.imread(path+"img2.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img1=cv2.resize(img1,(600,600))
img2=cv2.resize(img2,(600,600))

print(img1.shape,img2.shape)

#blending = a*img1+b*img2
blend=cv2.addWeighted(src1=img1,alpha=0.3,src2=img2,beta=0.7,gamma=0)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

plt.figure()
plt.imshow(blend)

plt.show()

