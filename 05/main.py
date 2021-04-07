import cv2
import numpy as np

rectangle = np.zeros((500, 500, 3), dtype="uint8")
cv2.rectangle(rectangle, (60, 60), (300, 200), (255, 255, 255), -1)
cv2.imshow("Rectangle", rectangle)


circle = np.zeros((500, 500, 3), dtype="uint8")
cv2.circle(circle, (250, 250), 150, (255, 255, 255), -1)
cv2.imshow("Circle", circle)

img = cv2.imread("./500.jpg")

mask = cv2.bitwise_xor(circle, img)
cv2.imshow("masked_c", mask)

mask = cv2.bitwise_and(rectangle, img)
cv2.imshow("masked_r", mask)


cv2.waitKey(0)
