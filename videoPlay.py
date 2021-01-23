import cv2
import time

#MOT17-04-DPM

name="MOT17-04-DPM.mp4"

cap=cv2.VideoCapture(name)

print("genislik:",cap.get(3))
print("yukseklik:",cap.get(4))


while cap.isOpened():
    _,frame=cap.read()
    #time.sleep(0.01)
    cv2.imshow('video',frame)

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

