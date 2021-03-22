import numpy as np
import cv2 as cv
import os
import time

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Han Solo', 'Leia', "Luke"]

# features = np.load('features.npy')
# labels = np.load('labels.npy')


face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_trained.yml')


img1 = cv.imread(
    r"aula16\val\Star_Wars_Empire_Strikes_Back_Han_Solo_Jacket__57700_zoom.jpg")

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img1, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)

    cv.rectangle(img1, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

cv.imshow('Detected face 1 ', img1)

img2 = cv.imread(
    r"aula16\val\ee0134647c17b777d15de15966cbec56.jpg")

gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img2, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)

    cv.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

cv.imshow('Detected face 2 ', img2)

img3 = cv.imread(
    r"aula16\Luke\hamill-new-hope.jpg")

gray = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img3, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)

    cv.rectangle(img3, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

cv.imshow('Detected face 3 ', img3)


cv.waitKey(0)
