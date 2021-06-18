import os
import cv2 as cv
import numpy as np

pessoas = ['DinossauroBebado']
DIR = r'Me_reconhecer\Pessoas'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

caracteristicas = []
etiqueta = []


def create_train():
    for person in pessoas:
        path = os.path.join(DIR, person)
        label = pessoas.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            cinza = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                cinza, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = cinza[y:y+h, x:x+w]
                caracteristicas.append(faces_roi)
                etiqueta.append(label)


create_train()
print('-----------------TREINAMENTO COMPLETO ---------------')

caracteristicas = np.array(caracteristicas, dtype='object')
etiqueta = np.array(etiqueta)

reco_face = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
reco_face.train(caracteristicas, etiqueta)

reco_face.save('treinado_DINO.yml')
np.save('caracteristicas.npy', caracteristicas)
np.save('etiqueta.npy', etiqueta)
