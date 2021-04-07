import cv2
import numpy as np
img = cv2.imread("./download.png")
cv2.imshow("image", img)

(B, G, R) = cv2.split(img)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)

zero = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("BB", cv2.merge([B, zero, zero]))
cv2.imshow("GG",  cv2.merge([zero, G, zero]))
cv2.imshow("RR",  cv2.merge([zero, zero, R]))

cv2.waitKey(0)
