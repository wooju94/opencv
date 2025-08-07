import cv2

#ROI(Refion of Interest) : 관심 영역

img = cv2.imread('./images/sun.jpg')

x = 182
y = 22
w = 117
h = 108

roi = img[y:y+h, x:x+w]
roy_copy = roi.copy()
img[y:y+h, x+w:x+w+w] =roi

drawing = False
oldx = oldy = 0
def on_mouse(event, x, y, param,flags):
    global oldx, oldy, drawing
    # print(event)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        oldx, oldy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy =img.copy()
            print('사각형 그리기')
            cv2.rectangle(img, (oldx, oldy,drawing), (x, y), (255, 51, 255), 3)
            cv2.imshow('img', img)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.rectangle(img, (oldx, oldy,drawing), (x, y), (255, 51, 255), 3)





cv2.imshow('img',img)
cv2.setMouseCallback('img', on_mouse)
cv2.waitKey()