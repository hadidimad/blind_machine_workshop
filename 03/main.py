import cv2
import numpy as np
import imutils
img = cv2.imread("./500.jpg")
value = np.ones((500, 500, 3), dtype="uint8")*100
value[0:500, 0:500] = (100, 100, 0)
added = cv2.add(img, value)
subbed = cv2.subtract(img, value)
cv2.imshow("added", added)
cv2.imshow("subbed", subbed)

cv2.imshow("normal", img)

cv2.waitKey(0)
