import cv2 as cv
import numpy as np


blank = np.zeros((400, 400), dtype='uint8')

rectangulo = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('retangulo', rectangulo)
cv.imshow('circulo', circle)

# bitwise and
#
biteise_and = cv.bitwise_and(rectangulo, circle)
cv.imshow('and', biteise_and)

# bitwise or

bitwise_or = cv.bitwise_or(rectangulo, circle)
cv.imshow("or", bitwise_or)

# bitwise xor
bitwise_xor = cv.bitwise_xor(rectangulo, circle)
cv.imshow("xor", bitwise_xor)
# bitwise not

bitwise_not = cv.bitwise_not(rectangulo)

bitwise_notd = cv.bitwise_not(circle)
cv.imshow('not', bitwise_not)
cv.imshow('notd', bitwise_notd)
cv.waitKey(0)
