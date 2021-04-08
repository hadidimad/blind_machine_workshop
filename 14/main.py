import cv2
import numpy as np
import mahotas


img = cv2.imread("./desk.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 1)
cv2.imshow("filterd", blur)

T = mahotas.thresholding.otsu(blur)

thresh = gray.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
print("Otsu’s threshold: {}".format(T))
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

T = mahotas.thresholding.rc(blur)
print("Riddler-Calvard: {}".format(T))
thresh = gray.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)

cv2.waitKey(0)
