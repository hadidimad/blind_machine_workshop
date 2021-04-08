import cv2
from matplotlib import pyplot as plt

img = cv2.imread("./500.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

cv2.imshow("img", gray)

eq = cv2.equalizeHist(gray)
histEq = cv2.calcHist([eq], [0], None, [256], [0, 256])

cv2.imshow("eq", eq)

plt.figure()
plt.plot(hist, color="red")
plt.plot(histEq, color="blue")
plt.show()

cv2.waitKey(0)
