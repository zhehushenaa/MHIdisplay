import cv2
import numpy
cap = cv2.VideoCapture("1.mp4")
while 1:
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()