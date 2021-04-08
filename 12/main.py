import cv2
import numpy as np

img = cv2.imread("./desk2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 1)
cv2.imshow("filterd", blur)
(T, thresh) = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
thresh = cv2.medianBlur(thresh,7)

print(T)

mask= cv2.bitwise_and(img,img,mask=thresh)

cv2.imshow("tresh", thresh)
cv2.imshow("mask", mask)



cv2.waitKey(0)
