import cv2
import numpy as np

# read an image

img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")
img3 = cv2.imread("img3.png")
img4 = cv2.imread("img4.png")
gray_img3 = cv2.cvtColor(img4,cv2.COLOR_BGRA2GRAY)
# img2 = cv2.imshow("img2",img2)
# print(img4.shape)
# cv2.imshow("img3",img3)
cv2.imshow("image",gray_img3)
cv2.waitKey(0)