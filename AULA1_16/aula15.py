import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = cv.imread(r"aula16\Han_Solo\7842a0b87955ccb93aa87f03f2626443.jpg")
cv.imshow("han-solo", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3)

print(f'number of faces found = {len(face_rect)}')

for(x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)
cv.imshow("face detectada ", img)


cv.waitKey(0)
