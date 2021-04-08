import cv2
import numpy as np


img = cv2.imread("./desk2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 1)
cv2.imshow("filterd", blur)

canny = cv2.Canny(blur, 60, 210)
cv2.imshow("canny", canny)

cv2.waitKey(0)
