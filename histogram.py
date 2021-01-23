import numpy as np
import cv2
import matplotlib.pyplot as plt

path="C:/Users/Asus/Desktop/imageProcessingOpenCV/imgs/"

img1=cv2.imread(path+"red_blue.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.imshow(img1),plt.axis('off'),plt.title('Red Blue')

print(img1.shape)
img1_hist=cv2.calcHist([img1],channels=[0],mask=None,histSize=[256],ranges=[0,256])
print(img1_hist.shape)
plt.figure(),plt.plot(img1_hist),plt.title('Red Blue Histogram')

colors=("b","g","r")
plt.figure()
for i,c in enumerate(colors):
    hist=cv2.calcHist([img1],channels=[i],mask=None,histSize=[256],ranges=[0,256])
    plt.plot(hist,color=c)

#goldenGate Img
goldenGateImg=cv2.imread(path+"goldenGate.jpg")
goldenGateImg=cv2.cvtColor(goldenGateImg,cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(goldenGateImg)
print(goldenGateImg.shape)

mask=np.zeros(goldenGateImg.shape[:2],np.uint8)
plt.figure(),plt.imshow(mask,cmap='gray')

mask[1500:2000, 1000:2000]=255
plt.figure(),plt.imshow(mask,cmap='gray')

maskedImg=cv2.bitwise_and(goldenGateImg,goldenGateImg,mask=mask)
plt.figure(),plt.imshow(maskedImg)

goldeGateHist=cv2.calcHist([goldenGateImg],channels=[0],mask=mask,histSize=[256],ranges=[0,256])
plt.figure(),plt.plot(goldeGateHist),plt.title('Golden Gate Histogram')

#Histogram Esitleme
img=cv2.imread(path+'hist_equ.jpg',0)
plt.figure(),plt.imshow(img,cmap='gray')

img_hist=cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(),plt.plot(img_hist)

eq_hist=cv2.equalizeHist(img)
plt.figure(),plt.imshow(eq_hist,cmap='gray')

eq_hist=cv2.calcHist([eq_hist],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(),plt.plot(eq_hist)



 




plt.show()