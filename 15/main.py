import cv2
import numpy as np
import mahotas


img = cv2.imread("./desk2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 1)
cv2.imshow("filterd", blur)

lap = cv2.Laplacian(blur, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

sobelX = cv2.Sobel(blur, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(blur, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)

cv2.waitKey(0)
