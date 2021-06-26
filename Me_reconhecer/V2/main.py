import sys
import cv2 as cv
from identificar import pessoa
from identificar import bola

pessoas = ['Dinossauro Bebado']


video_capture = cv.VideoCapture(0)

while True:
    # captura os frame tudo
    ret, frame = video_capture.read()

    # chama a função para usar o reconhecimento facial
    pessoa(frame, pessoas)
    bola(frame)
   # mostra
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Fecha
video_capture.release()
cv.destroyAllWindows()
