import cv2
import numpy as np
img = cv2.imread("./download.png")
cv2.imshow("image", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)


HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", HSV)


LAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", LAB)

cv2.waitKey(0)
