import cv2

cap=cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,heigth)



while cap.isOpened():
    
    _,frame=cap.read()

    cv2.imshow('vid',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):break

cap.release()
cv2.destroyAllWindows()