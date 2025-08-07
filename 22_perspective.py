import cv2
import numpy as np

img = cv2.imread('./images/pic.jpg')

w, h = 600 , 400

srcQuad = np.array([
    [370,173],[1224,157],[1417,830],[209,849]
],np.float32
)

dstQuad = np.array (
    [[0,0],[w,0],[w,h],[0,h]],np.float32
)

# 투시 변환(Perspective Transform)
# 영상에서 원근감을 조절하거나 , 사각형을 반듯하게 펴주는 변환
# 변환 행렬을 만들어준다.
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad) 

# 최종 행렬 변환
dst = cv2.warpPerspective(img,pers,(w,h))

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey()
