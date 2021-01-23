import numpy as np 
import cv2
import matplotlib.pyplot as plt 

path="C:/Users/Asus/Desktop/imageProcessingOpenCV/imgs/"
img=cv2.imread(path+'sudoku.jpg',0)

plt.imshow(img,cmap='gray'), plt.axis('off'),plt.title('Original Image')

#x gradyan
sobelX=cv2.Sobel(img,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=5)
plt.figure(),plt.imshow(sobelX,cmap='gray'), plt.axis('off'),plt.title('SobelX Image')

#y gradyna
sobelY=cv2.Sobel(img,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=5)
plt.figure(),plt.imshow(sobelY,cmap='gray'), plt.axis('off'),plt.title('SobelY Image')

#laplacian gradyan
laplacian=cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian,cmap='gray'), plt.axis('off'),plt.title('Laplacian Image')

plt.show()