from treinamento import treina
from reconhece import reconhece
import cv2 as cv
# treinar o reconhecimento de face

# treina()
img = 'DinossauroBebado\IMG_1767.JPG'

reconhece(img, "caracteristicas.npy", "etiquetas.npy",
          "reconhecimento_de_face_treinado_DINO.yml")
