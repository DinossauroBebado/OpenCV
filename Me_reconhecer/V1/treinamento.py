import cv2 as cv
import os
import numpy as np

nomes = ['DinossauroBebado']
DIR = r'DinossauroBebado'

haar_cascade = cv.CascadeClassifier("haar_face.xml")

features = []
labels = []


def parser_das_fotos():

    # entrar na pasta com as fotos

    label = 0

    # passar pelas imagens na pasta
    for img in os.listdir(DIR):
        img_path = os.path.join(DIR, img)

        img_array = cv.imread(img_path)
        cinza = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

        # acha a cara e passa as cordenadas
        faces_rect = haar_cascade.detectMultiScale(
            cinza, scaleFactor=1.1, minNeighbors=4)

        for(x, y, w, h) in faces_rect:
            # recorta a face da imagem
            faces_roi = cinza[y:y+h, x:x+w]
            # faz uma lista de caras
            features.append(faces_roi)
            # coloca a etiqueta com o nome certo
            labels.append(label)


def cria_treinamento(features, labels):

    features = np.array(features, dtype="object")
    labels = np.array(labels)

    # salva os arrays com as etiquetas com o nome das pessoas e as suas caras
    np.save("etiquetas.npy", labels)
    np.save("caracteristicas.npy", features)

    reconhecimento_de_face = cv.face.LBPHFaceRecognizer_create()  # crio o objeto

    reconhecimento_de_face.train(features, labels)  # treino

    # salva o modelo de treinamento para reproduzir
    reconhecimento_de_face.save("reconhecimento_de_face_treinado_DINO.yml")


def treina():
    # treinar o reconhecimento de face
    parser_das_fotos()
    cria_treinamento(features, labels)
