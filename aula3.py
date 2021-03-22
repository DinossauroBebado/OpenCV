import cv2 as cv
import numpy as np


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Preto", blank)


img = cv.imread("Laio.JPG")
cv.imshow("laio", scale(img, 0.2))
# pintar a imagem com certa cor
blank[:] = 0, 255, 0
cv.imshow("Verde", blank)
# desenhar um retangulo
cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=2)

cv.rectangle(blank, (400, 400), (300, 200), (255, 0, 0), thickness=cv.FILLED)

cv.imshow("retangulo", blank)
# desenhar um circulo
cv.circle(blank, (300, 100), 50, (0, 0, 0), thickness=3)
cv.imshow("circulo", blank)

# desenhar um linha
cv.line(blank, (500, 0), (0, 500), (255, 255, 255), thickness=30)
cv.imshow("linha", blank)
# escrever texto
cv.putText(blank, 'Dinossauro bebado', (200, 400),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 0), thickness=2)
cv.imshow("texto", blank)
cv.waitKey(0)
