import cv2

#HSV
# 색을 표현하는 한 방식으로 이미지 처리와 색상 추출에서 매우 자주 사용되는 장점을 가짐
# H: 색상(빨강, 초록, 파랑 등, 0~179), S: 채도(색의 선명함,0~255), V: 명도(밝기,0~255)

img = cv2.imread('./images/candies.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


airplane = cv2.imread('./images/airplane.bmp')
mask = cv2.imread('./images/mask_plane.bmp')
field = cv2.imread('./images/field.bmp')

'''
색상 H 값 (OpenCV 기준)     
빨강 (Red) 0 또는 179   
주황 (Orange) 10~20   
노랑 (Yellow) 20~30  
초록 (Green) 40~85   
파랑 (Blue) 90~130   
보라 (Violet) 130~160

채도 : 150 ~ 255
명도 : 0 ~ 255
'''
dst = cv2.inRange(hsv,(90, 150, 0),(130, 255, 255)) # 90~130 ,150~255 , 0 ~ 255

#copyTo 
# 마스크를 이용해서 선택적 복사 
temp = cv2.copyTo(airplane,mask) # mask에 있는부분을 복사해서 붙여준다.
cv2.copyTo(airplane,mask,field) # airplane 에서 mask를 복사해 field에 넣어준다.

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('temp',temp)
cv2.imshow('field',field)

cv2.waitKey()