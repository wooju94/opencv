import cv2
import matplotlib.pyplot as plt
import numpy as np

# 원본 이미지 읽기
img = cv2.imread('./images/dog.bmp')  # BGR 포맷
# img = cv2.imread('./images/gaussian_noise.jpg')
dst1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # RGB로 변환하여 plt에 적합하게

# GaussianBlur
# 픽셀 주변 값들을 가우시안 분포에 따라 가중 평균에서 흐리게 만듦
# 커널 크기가 클수록 넓은 범위를 흐리게 함
# 전체적으로 필터처리를 하고 싶을때
dst2 = cv2.GaussianBlur(img,(0,0),2) 

# 픽셀 주변의 값 중에서 중간값을 선택해서 새로운 픽셀 값으로 바꾸는 것
# 이미지의 각 픽셀을 기준으로 주변 픽셀을 확인한 후 그 중에서 가장 중간값(순서대로 정렬)을 가져와서 그 픽셀을 새로운 값으로 바꿔 블러 처리 함
dst3 = cv2.medianBlur(img,7)

# bilateralFilter : 양방향 필터
# 엣지(윤곽선)을 보전하면서 부드럽게 처리할 수 있는 필터
# 공간 정보 + 픽셀 색상 정보를 함께 고려
# 색상 거리 시그마, 공간 거리 시그마(30,30)
# 노이즈를 줄이고, 윤곽선을 유지하고 싶을 때 
dst4 = cv2.bilateralFilter(img,15,30,30)

#Canny 엣지 검출
# 엣지를 찾기 위한 임계값을 자동으로 조절하여 엣지를 찾아주는 알고리즘
# lower threshold : 약한 엣지를 설정
# upper threshold :  강한 엣지를 설정
med_val = np.median(img)
lower = int(max(0,0.7*med_val))
upper = int(min(255,1.3*med_val))
print(lower)
print(upper)

dst5 = cv2.GaussianBlur(img,(3,3),0)
dst5 = cv2.Canny(dst5,lower,upper,3)



# OpenCV로 보여주기 (BGR 기반이므로 원본과 dst1이 다르게 보일 수 있음)
cv2.imshow('Original BGR (cv2)', img)
cv2.imshow('RGB Image (cv2)', dst1)  # RGB지만 OpenCV는 BGR로 인식함 → 색 틀어져 보일 수 있음
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.imshow('dst5',dst5)

# Matplotlib로 필터링 결과 비교 시각화
plt.figure(figsize=(10, 5))
for i, k in enumerate([5, 7, 9]):
    # k*k 크기 커널 생성 : 예) k=5 1/25로 채워진 5*5 행렬
    kernel = np.ones((k, k)) / (k ** 2)
    #dst1 : 영상 , -1: 출력 이미지의 채널을 동일하게, 
    filtering = cv2.filter2D(dst1, -1, kernel)  # RGB 이미지에 필터 적용
    plt.subplot(1, 3, i + 1)
    plt.title(f'kernel size: {k}')
    plt.imshow(filtering)  
    plt.axis('off')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
