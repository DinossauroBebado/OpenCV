import cv2 as cv
import numpy as np

# Contorno


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = scale(cv.imread("NZ.JPG"), 0.2)
cv.imshow("NZ", img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Nz noir", gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(blur, 125, 150)
cv.imshow("cany", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)  # *
cv.imshow('thesh', thresh)

contorno, hierarquia = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # *
print(len(contorno))


cv.drawContours(blank, contorno, -1, (0, 0, 255), 2)

cv.imshow("blanlk", blank)

cv.waitKey(0)
