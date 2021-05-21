from datetime import datetime

import numpy as np
import cv2
import time
import base64

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
# while True:
#     time.sleep(10)
#     ret, frame = cap.read()
#     result, frame = cv2.imencode('.bmp', frame, [cv2.IMWRITE_WEBP_QUALITY, 100])
#     print('----------encode-----------')
#     print(result)
#     print('encode Image : ', frame)
#     b64data = base64.b64encode(frame)
#     print('encode -> base64 : ', b64data)
#     #위까지 base64로 인코딩  아래부터는 디코딩
#     print('---------decode---------')
#     frame = base64.b64decode(b64data)
#     print('decodebase64 : ', frame)
#     froms = np.frombuffer(frame, dtype='uint8')
#     print('?? : ', froms)
#     frame = cv2.imdecode(froms,cv2.IMREAD_COLOR)
#     cv2.imshow("test", frame)
#     if cv2.waitKey(1) > 0: break
# cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)    # 0번 카메라 연결
if cap.isOpened:
    file_path = 'C:/Users/hyeri/Desktop/record.avi'    # 저장할 파일 경로 이름 ---①
    fps = 30.0                     # FPS, 초당 프레임 수
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 인코딩 포맷 문자
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))                        # 프레임 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size) # VideoWriter 객체 생성
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recording',frame)
            out.write(frame)                        # 파일 저장
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            print("no frame!")
            break
    out.release()                                   # 파일 닫기
else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()