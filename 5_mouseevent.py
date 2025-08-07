import cv2
import numpy as np

oldx = oldy = 0
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    # print(event)
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼이 눌렸어요: %d, %d' % (x, y))
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 떼졌어요: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스가 이동하고 있어요: %d, %d' % (x, y))
        if flags:
            print('드래그중이에요')
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3)
            cv2.imshow('img', img)
            oldx, oldy = x, y


img = np.ones((500, 500, 3), dtype=np.uint8) * 255
cv2.namedWindow('img')


cv2.rectangle(img,(50,200,150,100),(0,255,0),3) # 이미지에 창 만들기
cv2.rectangle(img,(300,200,150,100),(0,255,0),-1) # 이미지에 창 만들기

cv2.circle(img,(150,400),50,(255,0,0),3) # 서클 만들기

cv2.putText(img,'Hello',(50,300), cv2.FONT_HERSHEY_DUPLEX,0.7,(0,0,0))

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()