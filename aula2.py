import cv2 as cv
# read image


def rescaleFrame(frame, scale):
    # funciona para video,imagem,live
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)
    dimensoes = (largura, altura)

    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


def changeRes(wight, height):
    # funciona para live video
    video.set(4, height)
    video.set(3, wight)


img = cv.imread("Laio.JPG")

cv.imshow("Laio", img)

resizedImage = rescaleFrame(img, 0.25)
cv.imshow('Lainho', resizedImage)

video = cv.VideoCapture("video.mp4")
while True:
    isTrue, frame = video.read()

    frameResizes = rescaleFrame(frame, 0.2)
    frameResizes1 = rescaleFrame(frame, 0.5)

    cv.imshow('video', frame)
    cv.imshow('video resized', frameResizes)
    cv.imshow('video resized 1 ', frameResizes1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
