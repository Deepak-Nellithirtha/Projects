import cv2
cap = cv2.VideoCapture(0)

while True:
   ret,frame = cap.read()
   canny = cv2.Canny(frame, 100, 200)
   cv2.imshow('My Live Life Sketch', canny)
   if cv2.waitKey(1) == 13:
       break

cap.release()
cv2.destroyAllWindows()