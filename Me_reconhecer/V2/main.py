import sys
import cv2 as cv


faceCascade = cv.CascadeClassifier('haar_face.xml')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('treinado_DINO.yml')
people = ['Dinossauro Bebado']
TOLERANCIA = 100

video_capture = cv.VideoCapture(0)

while True:
    # captura frame por frame
    ret, frame = video_capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),

    )

    for (x, y, w, h) in faces:

        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')
        if confidence > TOLERANCIA:
            continue
        cv.putText(frame, str(people[label]), (x, y),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=1)
        cv.putText(frame, str(confidence)[:2], (x, y+h),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=1)

        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), thickness=1)

   # mostra
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Fecha
video_capture.release()
cv.destroyAllWindows()
