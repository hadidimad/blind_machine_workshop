import numpy as np
import cv2
import mahotas

cap = cv2.VideoCapture(0)

clicking = False
croped = False
points = []
frame = None
mouseX = 0
mouseY = 0


def mouse_handler(event, x, y, flags, param):
    global clicking, points, mouseX, mouseY,croped
    if event == cv2.EVENT_LBUTTONDOWN:
        croped = False
        print("button down")
        points = [(x, y)]
        clicking = True
    elif event == cv2.EVENT_LBUTTONUP:
        print("button up")
        points.append((x, y))
        clicking = False
        croped = True
    mouseX = x
    mouseY = y


cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_handler)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if clicking:
        gray = cv2.rectangle(gray, points[0], (mouseX, mouseY), (255, 0, 0), 2)
    if croped:
        print("cropped")
        gray = gray[points[0][1]:points[1][1],points[0][0]:points[1][0]]
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
