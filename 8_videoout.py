import cv2

cap1 = cv2.VideoCapture('./movies./istockphoto-524804954-640_adpp_is.mp4')
cap2 = cv2.VideoCapture('./movies/istockphoto-1194080385-640_adpp_is.mp4')

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter.fourcc(*'DIVX')  # 동영상 압축기술 'DIVX' = avi
out = cv2.VideoWriter('mix.avi', fourcc, fps, (w, h)) 

for i in range(frame_cnt1):
    ret, frame = cap1.read()
    cv2.imshow('output', frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('output', frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release() 