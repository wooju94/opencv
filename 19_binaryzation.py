# 이진화 
# 이미지의 픽셀 값을  0 과 1(0과 255) 두 가지 값만 가지도록 만드는 영상 처리 기법
# OCR, 윤곽 검출, 객체 분할, 문서스캔 등 작업에 유리

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/cells.png', cv2.IMREAD_GRAYSCALE)
hist  = cv2.calcHist([img], [0],None,[256],[0,255])

 # 필셀값이 임계값을 넘으면 최댓값으로 설정 넘지 못하면 0으로 설정 
 # 100이하 0 : 까맣게  # 이상 255 : 더 하얗게
a,dist1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) 
print(a)

b,dist2 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY) 
print(b)

# 오츠 이진화 임계값 206
c, dst3 = cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(c)

cv2.imshow('img',img)
cv2.imshow('dst1',dist1)
cv2.imshow('dst2',dist2)
cv2.imshow('dst3',dst3)
plt.plot(hist)
plt.show()
cv2.waitKey()


