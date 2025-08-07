import cv2
import sys

cap = cv2.VideoCapture('./movies/istockphoto-524804954-640_adpp_is.mp4')

if not cap.isOpened():
    print('동영상을 불러올수 없음')
    sys.exit() # 프로그램 종료
    
print('동영상을 불러올 수 있음')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)# 넓이
print(width)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)# 높이
print(height)

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) #프레임 개수
print(frame_count)

fps = cap.get(cv2.CAP_PROP_FPS) # 1초에 몇개의 이미지가 지나가는가
print(fps)

while True:
    ret,frame = cap.read()                  # cap.read() 프레임 1장을 가져와라
    if not ret:                            # ret = 1장이 들어오면 True 표시 ,frame = 이미지 1장 
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) ==27:
        break 

cap.release()                                      