import cv2 as cv
import numpy as np


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = scale(cv.imread("NZ.jpg"), 0.2)
cv.imshow("NZ", img)

# average

average = cv.blur(img, (7, 7))
cv.imshow("average blur", average)

# gausian blur

gausian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("gausian", gausian)

# median blur
median = cv.medianBlur(img, 7)
cv.imshow("median", median)

# bilateral

# img,diametro, aumenta as cores proximas q vao ser consideradas na conta,quanto distante um pixel vai influenciar o pixel
bilateral = cv.bilateralFilter()
cv.imshow("bilateral", bilateral)


cv.waitKey(0)
