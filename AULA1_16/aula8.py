import cv2 as cv
import numpy as np


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = scale(cv.imread("NZ.JPG"), 0.2)
cv.imshow("NZ", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("red", red)
cv.imshow('blue', blue)
cv.imshow('green', green)
# aonde esta escuro é que nao tem essa cor
print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)
# juntar esses canais de cor juntos
merged = cv.merge([b, g, r])
cv.imshow("merged", merged)


cv.waitKey(0)
