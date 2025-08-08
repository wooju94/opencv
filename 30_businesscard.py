import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np

card = cv2.imread('./images/businesscard.jpg')

plt.imshow(cv2.cvtColor(card,cv2.COLOR_BGR2RGB))
plt.title('card')
plt.axis('off')
plt.show()

# 윤곽선 뽑기 노이즈 제거

gray = cv2.cvtColor(card,cv2.COLOR_BGR2GRAY) 
blur = cv2.GaussianBlur(gray,(5,5),0)

# 윤곽선 추출 엣지 검출 Canny
edge = cv2.Canny(blur,50,150)

# 윤곽선 찾기
contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# 윤곽선 크기순 정렬 (가장 큰 사각형 찾아내기)
contours = sorted(contours, key = cv2.contourArea, reverse=True)

for cnt in contours:
    # 윤곽선 단순화
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    if len(approx) == 4:
        doc_cnt = approx
        break

def order_points(pts):
    pts = pts.reshape(4,2)
    rect = np.zeros((4,2), dtype = 'float32')

    s = pts.sum(axis = 1)
    diff = np.diff(pts, axis=1)

    rect[0] = pts[np.argmin(s)] # 좌상
    rect[2] = pts[np.argmax(s)] # 우하
    rect[1] = pts[np.argmin(diff)] # 우상
    rect[3] = pts[np.argmax(diff)] # 좌하

    return rect

rect = order_points(doc_cnt)

# 펼칠 너비/높이 계산
(tl, tr, br, bl) = rect
widthA = np.linalg.norm(br - bl)
widthB = np.linalg.norm(tr - tl)
heightA = np.linalg.norm(tr - br)
heightB = np.linalg.norm(tl - bl)

maxWidth = int(max(widthA, widthB))
maxHeight = int(max(heightA, heightB))

# 투시변환 수행
dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]
], dtype="float32")

M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(card, M, (maxWidth, maxHeight))

plt.imshow(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
plt.title("펼친 명함 이미지")
plt.axis('off')
plt.show()

gray_wraped = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)

# OCR 수행

text = pytesseract.image_to_string(gray_wraped, lang ='eng+kor')
print('텍스트',text)


#---------------------------------------------------------------------------------------

# 두번째 busunesscard

import cv2
import pytesseract
import numpy as np
'''
[[903. 199.]
 [179. 200.]
 [159. 593.]
 [938. 581.]]
'''
def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))
    pts = pts[idx]
    print(pts)
    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]
    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]
    print(pts)
    return pts
img = cv2.imread('./images/businesscard2.jpg')
dw, dh = 700, 400
srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
dst = np.zeros((dh, dw), np.uint8)
src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cpy = img.copy()
for pts in contours:
    if cv2.contourArea(pts) < 500:
        continue
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2)
    print(approx)
    print(approx.reshape(4, 2).astype(np.float32))
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(img, pers, (dw, dh))
    dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    print(pytesseract.image_to_string(dst_gray, lang='kor+eng'))
    cv2.imshow('img', img)
    cv2.imshow('cpy', cpy)
    cv2.imshow('dst', dst)
    cv2.waitKey()





