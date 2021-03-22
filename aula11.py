import cv2 as cv
import numpy as np


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = scale(cv.imread("NZ.jpg"), 0.2)
cv.imshow("NZ", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("blank", blank)

mask = cv.circle(blank, (img.shape[1]//2-100,
                         img.shape[0]//2+150), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('masked', masked)

cv.waitKey(0)
