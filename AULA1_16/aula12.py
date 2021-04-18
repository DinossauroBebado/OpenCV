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

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("cinza", gray)j

# gray_hist = cv.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.title('color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 255])
# plt.show()

# -------------colorido
cores = ('b', 'r', 'g')
for i, col in enumerate(cores):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 255])

plt.show()

cv.waitKey(0)
