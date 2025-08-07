import cv2

img1 = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
print(img1)

img2 = cv2.imread('./images/dog.bmp')
print(img2)


cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey()