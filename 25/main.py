import cv2
import numpy as np


cap = cv2.VideoCapture(0)

background = None
chosed = False

while True:
    _, frame = cap.read()
    if chosed:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diffrence = cv2.absdiff(gray, background)
        diffrence = cv2.medianBlur(diffrence, 7)
        # diffrence = cv2.cvtColor(diffrence, cv2.COLOR_BGR2GRAY)
        _, diffrence = cv2.threshold(diffrence, 50, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(
            diffrence, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            if w*h > 2000:
                frame = cv2.rectangle(
                    frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord('b'):
        chosed = True
        background = frame.copy()
        background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
