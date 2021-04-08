from matplotlib import pyplot as plt
import cv2

img = cv2.imread("./500.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", gray)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure()
plt.plot(hist)
plt.show()

cv2.waitKey(0)
