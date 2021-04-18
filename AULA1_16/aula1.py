import cv2 as cv
# read image
"""img = cv.imread("Laio.JPG")

cv.imshow("Laio", img)

cv.waitKey(0)"""
# read video

video = cv.VideoCapture("video.mp4")
while True:
    isTrue, frame = video.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
