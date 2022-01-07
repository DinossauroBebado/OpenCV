import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier(r'data\haarcascade_frontalface_alt2.xml')

cam = cv.VideoCapture(0)

while(True):
    ret, frame = cam.read()

    cv.imshow('frame', frame)
    if cv.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
