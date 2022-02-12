import cv2 as cv
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5) -> None:
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils





  imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
  results = hands.process(imgRGB)
   # print(results.multi_hand_landmarks)

   if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 4:
                    cv.circle(img, (cx, cy), 25, (255, 0, 255), cv.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10, 70),
               cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cv.imshow('webcam', img)

    cv.waitKey(1)


def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70),
                   cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

        cv.imshow('webcam', img)

        cv.waitKey(1)


if__name__ == "__main__":
    main()