import cv2

img1 = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./images/dog.bmp')

dst1 = cv2.add(img1,100)
dst2 = cv2.add(img2,(100,100,100))
dst3 = cv2.subtract(img1,100) # -로 더 어둡게
dst4 = cv2.multiply(img1,10) # 곱하기
dst5 = cv2.divide(img1,10) # 나누기



cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.imshow('dst5',dst5)
cv2.waitKey()