# OCR(Optical Character ReCognition)
# 영상이나 문서에서 텏그트를 자동으로 인식하고 컴퓨터가 이행할 수 있는 텍스트 데이터로 변환하는 과정
# Tesseract,EasyOCR,paddleOCR, CLOVA OCR(네이버 API), Cloud Vision(구글 API)..

# 테서렉트 
# https://github.com/UB-Mannheim/tesseract/wiki

# 내 pc 오른쪽 클릭 => 고급 시스템 설정 => 환경변수 => path => 테서렉트OCR 폴더 경로 복사해서 추가 

import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/hello.png')
dst = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#lang = 'kor' # 출력할 이미지의 언어를 맞춰준다. 
text = pytesseract.image_to_string(dst, lang = 'kor+eng')
print(text)


