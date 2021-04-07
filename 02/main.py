import cv2
import numpy as np
import imutils
img = cv2.imread("./500.jpg")

M = np.float32([[1, 0, -300], [0, 1, -30]])
out = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("image", out)
cv2.waitKey(0)

out = imutils.translate(out, 300, 30)
cv2.imshow("image", out)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D((500, 500), 45, 1.0)
out = cv2.warpAffine(img, M, (900, 900))
cv2.imshow("image", out)
cv2.waitKey(0)


out = cv2.resize(img,(100,100))
out = cv2.resize(out,(500,500))

cv2.imshow("image", out)
cv2.waitKey(0)

out = img[100:200,100:300]
cv2.imshow("image", out)
cv2.waitKey(0)
