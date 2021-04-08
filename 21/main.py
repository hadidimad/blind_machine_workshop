import cv2
import numpy as np
boundaries = [(20, 20, 50), (80, 80, 255)]
img = cv2.imread("./balls.jpg")

mask = cv2.inRange(img, boundaries[0], boundaries[1])
img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("img", img)
cv2.imshow("mask", mask)

cv2.waitKey(0)
