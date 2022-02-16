import cv2 as cv
import time
import os

import HandTracking as ht

# documentation
# https://google.github.io/mediapipe/solutions/hands

DEBUG = False
wCam, hCam = 640, 480

cap = cv.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

detector = ht.handDetector(detectionCon=1)

# change for dict
tipIds = [4, 8, 12, 16, 20]


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    # search hand
    if(len(lmList) != 0):
        fingers = []
        # expeption thumb
        # right hand
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # exclude thumb
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        number_fingers = sum(fingers)
        if DEBUG:
            print(fingers, number_fingers)
        cv.putText(img, str(number_fingers), (10, 70),
                   cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cv.imshow("Image", img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
