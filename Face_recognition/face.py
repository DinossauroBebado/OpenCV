import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier(
    r'data\haarcascade_frontalface_alt2.xml')

cam = cv.VideoCapture(0)

while(True):
    # get camera frame
    ret, frame = cam.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)

    for(x, y, w, h) in faces:
        # region of intersted
        #roi_gray = gray[y:y+h, x:x+w]
        #img_item = "my_image.png"
        #cv.imwrite(img_item, roi_gray)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # display camera frame
    cv.imshow('frame', frame)
    if cv.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
