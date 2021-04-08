from matplotlib import pyplot as plt
import cv2

img = cv2.imread("./500.jpg")
cv2.imshow("image", img)
(B, G, R) = cv2.split(img)


histB = cv2.calcHist([B], [0], None, [256], [0, 256])
histG = cv2.calcHist([G], [0], None, [256], [0, 256])
histR = cv2.calcHist([R], [0], None, [256], [0, 256])


plt.figure()
plt.plot(histR, color="red")
plt.plot(histB, color="blue")
plt.plot(histG, color="green")
plt.show()

cv2.waitKey(0)
