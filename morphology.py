import cv2
import numpy as np 
import matplotlib.pyplot as plt

path="C:/Users/Asus/Desktop/imageProcessingOpenCV/imgs/"
img=cv2.imread(path+"j.png",0)

#original image
plt.imshow(img,cmap='gray'),plt.axis('off'),plt.title('Original Image'),

#ERODE
kernel=np.ones((5,5),dtype=np.uint8)
resultImg=cv2.erode(img,kernel,iterations=1)
plt.figure(),plt.imshow(resultImg,cmap='gray'),plt.axis('off'),plt.title('ERODE Image'),

#DILATION
resultImg2=cv2.dilate(img,kernel,iterations=1)
plt.figure(),plt.imshow(resultImg2,cmap='gray'),plt.axis('off'),plt.title('DILATION Image'),

#white noise
whiteNoise=np.random.randint(0,2,size=img.shape[:2])
whiteNoise=whiteNoise*255 
plt.figure(),plt.imshow(whiteNoise, cmap='gray'),plt.axis('off'),plt.title('Noises for Morphology')

noisy_img=whiteNoise+img
plt.figure(),plt.imshow(noisy_img, cmap='gray'),plt.axis('off'),plt.title('Noisey Image')

#morphologyEx(beyzları azalt erode, sonra dilation uygula)
openedImg=cv2.morphologyEx(img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure(),plt.imshow(openedImg, cmap='gray'),plt.axis('off'),plt.title('Opened Image')

#black noise for morphClose
blackNoise=np.random.randint(0,2,size=img.shape[:2])
blackNoise=whiteNoise*-255 
plt.figure(),plt.imshow(blackNoise, cmap='gray'),plt.axis('off'),plt.title('black noise for Morphology')

noisy_img2=blackNoise+img
noisy_img2[noisy_img2 <= -245] =0
plt.figure(),plt.imshow(noisy_img2, cmap='gray'),plt.axis('off'),plt.title('Black Noisy  Image')

closedImg=cv2.morphologyEx(img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure(),plt.imshow(closedImg, cmap='gray'),plt.axis('off'),plt.title('Black Noisy  Image after Closed morph')

#gradient  # basic edge detection 
gradient=cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel)
plt.figure(),plt.imshow(gradient, cmap='gray'),plt.axis('off'),plt.title('Gradian  Image')



plt.show()