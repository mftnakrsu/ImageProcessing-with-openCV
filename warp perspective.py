import cv2
import numpy as np

path="C:/Users/Asus/Desktop/imageProcessingOpenCV/kart.png"

img=cv2.imread(path)
cv2.imshow("Image perspective with OpenCV",img)

width=400
height=500

pts1=np.float32([[230,1],[1,472],[540,150],[338,617]])#take coordinates paint
pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

imgOut=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Final Image", imgOut)



cv2.waitKey(0)
cv2.destroyAllWindows()