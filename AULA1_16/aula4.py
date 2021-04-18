import cv2 as cv
import numpy as np


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = cv.imread("Laio.JPG")
cv.imshow("laio", scale(img, 0.2))

# converter a para grayscale

gray = cv.cvtColor(scale(img, 0.2), cv.COLOR_BGR2GRAY)
#cv.imshow("Laio noir", gray)

# BLUR
blur = cv.GaussianBlur(scale(img, 0.2), (11, 11), cv.BORDER_DEFAULT)
#cv.imshow("blur", blur)

img = scale(img, 0.2)

# edge cascade
# se quiser reduzir as linhas brancas pode aplicar um blur
cany = cv.Canny(img, 125, 175)
cv.imshow("canny", cany)

# dilating the image
dilated = cv.dilate(cany, (3, 3), iterations=1)
cv.imshow("dilated", dilated)

# eroding
erode = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("erode", erode)

# resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resize)

# cropping
cropped = img[50:200, 200:400]
cv.imshow("croped", cropped)

cv.waitKey(0)
