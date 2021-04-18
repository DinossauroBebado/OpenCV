import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import resize


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = scale(cv.imread("Laio.JPG"), 0.2)
cv.imshow("laio", img)

# translação eixo x e y


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensoes = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensoes)


# - x --> left
# -y --> up
# +x --> right
# +y --> down
translated = translate(img, 100, 100)
cv.imshow("translated", translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, widht) = img.shape[:2]

    if rotPoint is None:
        rotPoint = widht//2, height//2

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensoes = (widht, height)

    return cv.warpAffine(img, rotMat, dimensoes)


rotated = rotate(img, 45)
cv.imshow("rodado", rotated)

# resize

resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("resized", resize)

# flip
flip = cv.flip(img, 0)
'''0 = flip de imagem verticaly or the x exis
   1 = flip de image horizontaly or the y exis
   -1 = both verticaly and horizontaly '''
cv.imshow("flip", flip)

# cropping
cropped = img[50:200, 200:400]
cv.imshow("croped", cropped)

cv.waitKey(0)
