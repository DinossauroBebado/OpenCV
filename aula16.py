import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import time


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


DIR = r"aula16"

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Han Solo', 'Leia', "Luke"]

features = []

labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            #cv.imshow('teste', img_array)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for(x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]

                features.append(faces_roi)
                labels.append(label)


create_train()
print("Acabo companheiro")


features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)

np.save('labels.npy', labels)
