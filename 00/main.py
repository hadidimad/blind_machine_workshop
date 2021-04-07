import cv2

img = cv2.imread("./10.jpg")
img[1:5, 1:9] = (255, 0, 255)
img2 = img[1:5, 1:9]
cv2.imshow("image", img)
cv2.imshow("image2", img2)

cv2.imwrite("edit.jpg",img)
cv2.waitKey(0)
