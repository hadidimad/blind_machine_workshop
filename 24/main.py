import cv2
import numpy as np

img1 = cv2.imread("./p1.jpg")
img2 = cv2.imread("./p2.jpg")

cv2.imshow("one", img1)
cv2.imshow("two", img2)
out = img1.copy()

diffrence = cv2.absdiff(img1, img2)
diffrence = cv2.medianBlur(diffrence, 7)
diffrence = cv2.cvtColor(diffrence, cv2.COLOR_BGR2GRAY)
_, diffrence = cv2.threshold(diffrence, 20, 255, cv2.THRESH_BINARY)
cv2.imshow("difrecne", diffrence)

cnts, _ = cv2.findContours(
    diffrence, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    out = cv2.rectangle(out, (x, y), (x+w, y+h), (0, 0, 255), 5)
cv2.imshow("out", out)
cv2.waitKey(0)
