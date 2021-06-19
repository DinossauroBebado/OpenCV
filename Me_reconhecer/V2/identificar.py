import cv2 as cv
import numpy as np

faceCascade = cv.CascadeClassifier('haar_face.xml')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('treinado_DINO.yml')
TOLERANCIA = 100

verdeClaro = (29, 86, 6)  # modificar para um ajuste
verdeEscuro = (64, 255, 255)


def pessoa(frame, pessoas):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),

    )

    for (x, y, w, h) in faces:

        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {pessoas[label]} with a confidence of {confidence}')
        if confidence > TOLERANCIA:
            continue
        cv.putText(frame, str(pessoas[label]), (x, y),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=1)
        cv.putText(frame, str(confidence)[:2], (x, y+h),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=1)

        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), thickness=1)

    return frame


def bola(frame):

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, verdeClaro, verdeEscuro)

    kernel = np.ones((5, 5), np.uint8)
    mascE = cv.erode(mask, None, iterations=2)
    mascD = cv.dilate(mascE, None, iterations=2)

    cv.imshow('Video', mascD)
    return frame
