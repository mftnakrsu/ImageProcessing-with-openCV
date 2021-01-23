# opencv kütüphanesini içe aktaralım
import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi siyah beyaz olarak içe aktaralım
img=cv2.imread('odev1.jpg',0)

# resmi çizdirelim
plt.imshow(img,cmap='gray'),plt.axis('off'),plt.title('Homework Image')

# resmin boyutuna bakalım
print(img.shape)#560,860

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
resizedImg=cv2.resize(img,(int(568*0.8),int(860*0.8)))
plt.figure(),plt.imshow(resizedImg,cmap='gray'),plt.axis('off'),plt.title('Resized Image')

# orijinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
cv2.putText(img,'Cat and dog image',(100,150),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
plt.figure(),plt.imshow(img),plt.axis('off'),plt.title('Image with text')

# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim

_,imgThresh=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
plt.figure(),plt.imshow(imgThresh,cmap='gray'),plt.axis('off'),plt.title('ThreshHold Image')


# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
GaussianBluredImg=cv2.GaussianBlur(img,(5,5),0)
plt.figure(),plt.imshow(GaussianBluredImg,cmap='gray'),plt.axis('off'),plt.title('Gaussian Blured Image')


# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
laplacianGradImg=cv2.Laplacian(img,ddepth=cv2.CV_16S,ksize=3)
plt.figure(),plt.imshow(laplacianGradImg,cmap='gray'),plt.axis('off'),plt.title('with laplacian Image')


# orijinal resmin histogramını çizdirelim
img1_hist=cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
print(img1_hist.shape)
plt.figure(),plt.plot(img1_hist),plt.title('Histogram')



plt.show()













