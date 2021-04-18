import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier("haar_face.xml")


def reconhece(img, caracteristica, etiqueta_file, modelo_treinado):

    nomes = ["DinossauroBebado"]

    caracteristicas = np.load(caracteristica, allow_pickle=True)
    etiquetas = np.load(etiqueta_file)

    reconhecimento_de_face = cv.face.LBPHFaceRecognizer_create()
    reconhecimento_de_face.read(modelo_treinado)

    imagem = cv.imread(img)
    cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

    # detectar a face

    faces_rect = haar_cascade.detectMultiScale(
        cinza, scaleFactor=1.1, minNeighbors=4)

    for(x, y, w, h) in faces_rect:
        faces_roi = cinza[y:y+h, x:x+h]

        etiqueta, confianca = reconhecimento_de_face.predict(faces_roi)

        print(f"Nome = {nomes[etiqueta]} com uma confiança de {confianca}")
