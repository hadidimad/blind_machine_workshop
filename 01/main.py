import cv2
import numpy as np

canvas = np.zeros((500, 300, 3), dtype="uint8")

canvas = cv2.line(canvas, (100, 10), (10, 100), (0, 0, 255), 6)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

canvas = cv2.rectangle(canvas, (20, 30), (50, 80), (255, 0, 0), -1)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

canvas = cv2.circle(canvas, (250,150),40,(0,255,0))
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

