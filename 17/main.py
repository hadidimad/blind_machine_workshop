import cv2
import numpy as np


img = cv2.imread("./download.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 1)
cv2.imshow("filterd", blur)

canny = cv2.Canny(blur, 60, 180)
cv2.imshow("canny", canny)

# (_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts, hierarchy = cv2.findContours(
    canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} objects in this image".format(len(cnts)))

obj = img.copy()
cv2.drawContours(obj, cnts, -1, (0, 255, 0), 1)
cv2.imshow("obj", obj)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    if w*h > 500:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("img", img)


cv2.waitKey(0)
