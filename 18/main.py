import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('7.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('temp.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
cv2.imshow("res",res)

loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)

cv2.imshow("matched", img_rgb)
cv2.waitKey(0)
