import cv2
import numpy as np

img = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

# 전역 자동 이진화
a, dst1 = cv2.threshold(img, 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 자동 이진화
dst2 = np.zeros(img.shape, np.uint8)
bw = img.shape[1] // 4 # 이미지 4등분
bh = img.shape[0] // 4 # 이미지 높이 4등분

# 적응형 이진화
# cv2.ADAPTIVE_THRESH_MEAN_C :  해당 픽셀 주변에 평균값을 기준으로 임계값 설정
# 9 : 이웃 블록의 크기 , 현재 픽셀 주변에서 얼마만큼의 영역을 고려할지 설정(커널이라고 생각하면 편함), 블록사이즈가 클수록 더 넓은 영역을 평균 -> 조명에 덜 민감하지만 부드러움
# 5: 임계값 보정 상수, 평균 또는 가중 평균에서 얼마나 빼줄지 결정, 값이 클수록 픽셀이 어두워야 흰색이됨(임계값을 낮추거나 높이기 위한 튜닝용 파라미터)
dst3 = cv2.adaptiveThreshold(img,  255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,5)

#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 주변 픽셀에 가중치를 곱한 평균값으로 임계값 설정
# 조명이 불균일한 이미지에서 효과적 , 부드러운 결과를 준다. 

dst4 = cv2.adaptiveThreshold(img,  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,9,5)

for y in range(4):
    for x in range(4):
       # img 크기와 똑같이 맞춰줘야 dst_에 넣을 수 있다. 
       img_ = img[y*bh:(y+1)*bh, x*bw: (x+1)*bw]
       dst_ = dst2[y*bh:(y+1)*bh, x*bw : (x+1)*bw]
       cv2.threshold(img_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)
        # dst_에 넣어라



cv2.imshow('img',img)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)

cv2.waitKey()