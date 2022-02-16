import cv2 as cv
import time
import os

import HandTracking as ht

DEBUG = True
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
        # expeption tumb
        if lmList[tipIds[id]][1] < lmList[tipIds[id] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # exclude tumb
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        if DEBUG:
            print(fingers)

    cv.imshow("Image", img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
