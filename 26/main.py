import numpy as np
import cv2


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("./face_cascade.xml")
eye_cascade = cv2.CascadeClassifier('./eye_cascade.xml')

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 8)
    eyes = eye_cascade.detectMultiScale(gray, 1.8, 15)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
