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
cv.imshow('Gray', gray)

# simple treshhold

treshold, tresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow("simple trash", tresh)

treshold, tresh_inverse = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple trash", tresh_inverse)

# adaptive Thresholding

adaptive_tresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 5)
cv.imshow("Adaptive", adaptive_tresh)

cv.waitKey(0)
