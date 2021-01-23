import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

path="C:/Users/Asus/Desktop/imageProcessingOpenCV/imgs/"


#blurring detayı azalt, gürültüyü engeller
img=cv2.imread(path+'NYC.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(img), plt.axis('off'), plt.title('Original')

#mean blurring
dst2=cv2.blur(img,(3,3))
#plt.figure(),plt.imshow(dst2),plt.axis('off'),plt.title('Mean Blurring')

#Gaussian blurring
gb=cv2.GaussianBlur(img,(3,3),7)
#plt.figure(),plt.imshow(gb),plt.axis('off'),plt.title('Gauissian Blurring')

#Median blurring
mb=cv2.medianBlur(img,3)
#plt.figure(),plt.imshow(mb),plt.axis('off'),plt.title('Median Blurring')

#%%
def gausNoise(image):
    row, col, ch=image.shape
    mean=0
    var=0.05
    sigma=var**0.5

    gauss=np.random.normal(mean,sigma,(row,col,ch))
    gauss=gauss.reshape(row,col,ch)
    noisy=image+gauss

    return noisy

#Normalization
img=cv2.imread(path+'NYC.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
plt.imshow(img), plt.axis('off'), plt.title('Original')

plt.figure()
noisyImage=gausNoise(img)
plt.imshow(noisyImage), plt.axis('off'), plt.title('Noisy Image')

#Blurring with noisy image
gb2=cv2.GaussianBlur(noisyImage,(3,3),7)
plt.figure(),plt.imshow(gb2),plt.axis('off'),plt.title('with Gauissian Blurring')

#%%
#salt pepper noise

def saltPepperNoise(img):
    row, col, ch=img.shape
    s_vs_p=0.5
    amount=0.004
    noisy=np.copy(img)

    num_salt=np.ceil(amount*img.size*s_vs_p)
    coords=[np.random.randint(0,i-1, int(num_salt)) for i in img.shape]
    noisy[coords]=1

    num_pepper=np.ceil(amount*img.size*s_vs_p)
    coords=[np.random.randint(0,i-1, int(num_pepper)) for i in img.shape]
    noisy[coords]=0

    return noisy

spImage=saltPepperNoise(img)

plt.figure()
plt.imshow(spImage), plt.axis('off'), plt.title('saltPapper Image')

#Median blurring
mb2=cv2.medianBlur(spImage.astype('float32'),3)
plt.figure(),plt.imshow(mb2),plt.axis('off'),plt.title('with Median Blurring')


plt.show()

