import cv2 as cv
import numpy as np


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


img = scale(cv.imread("NZ.JPG"), 0.2)
cv.imshow("NZ", img)

# BGR --> grey

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("NZ noir", grey)

# BGR --> HSV Hue Saturaion Value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsc", hsv)

# BGR to Lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

cv.imshow("lab", lab)

# BGR --> RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)


cv.waitKey(0)
