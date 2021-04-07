import cv2
import numpy as np

rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)


circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)


bitAnd= cv2.bitwise_and(circle,rectangle);
cv2.imshow("and", bitAnd)

bitor= cv2.bitwise_or(circle,rectangle);
cv2.imshow("or", bitor)

bitxor= cv2.bitwise_xor(circle,rectangle);
cv2.imshow("xor", bitxor)
img=cv2.imread("./500.jpg")

bitnot= cv2.bitwise_not(img);
cv2.imshow("not", bitnot)

cv2.waitKey(0)
