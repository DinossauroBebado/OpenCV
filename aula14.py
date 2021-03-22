import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = scale(cv.imread("NZ.jpg"), 0.2)
cv.imshow("NZ", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplacian

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("laplacian", lap)

# sobel

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)

sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("X", sobelx)

cv.imshow("Y", sobely)

cv.imshow("X&Y", combined_sobel)

cany = cv.Canny(gray, 150, 175)
cv.imshow('CANNY', cany)

cv.waitKey(0)
