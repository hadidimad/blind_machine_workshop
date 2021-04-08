import cv2
import numpy as np

img = cv2.imread("./500.jpg")
noise=cv2.imread("./noisy.png")
blur3 = cv2.blur(img, (3, 3))
blur5 = cv2.blur(img, (5, 5))
blur7 = cv2.blur(img, (7, 7))

GaussianBlur3 = cv2.GaussianBlur(img, (3, 3), 0)
GaussianBlur5 = cv2.GaussianBlur(img, (5, 5), 0)
GaussianBlur7 = cv2.GaussianBlur(img, (7, 7), 0)


medianBlur3 = cv2.medianBlur(img, 3)
medianBlur5 = cv2.medianBlur(img, 5)
medianBlur7 = cv2.medianBlur(img, 7)

cv2.imshow("orginal", img)
cv2.imshow("avrage", np.hstack((blur3, blur5, blur7)))
cv2.imshow("gausssian", np.hstack(
    (GaussianBlur3, GaussianBlur5, GaussianBlur7)))

cv2.imshow("median", np.hstack(
    (medianBlur3, medianBlur5, medianBlur7)))


cv2.waitKey(0)
