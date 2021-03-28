import numpy as np
import cv2
from datetime import datetime, timedelta
import encrypt
import imageio
import matplotlib.pyplot as plt

xml = '/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)

cap = cv2.VideoCapture(0)  # 노트북 웹캠을 카메라로 사용
cap.set(3, 640)  # 너비
cap.set(4, 480)  # 높이

time = datetime.now()
i = 0
while (True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # 좌우 대칭
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.05, 5)
    print(time)

    if len(faces):
        if ret:
            time2 = datetime.now()
            print((time2 - time).microseconds)
            # 시간값도 설정하기
            if (time2 - time).microseconds >= 30000:
                name = "C:/opencv/photo" + str(i) + ".jpg"
                print(name)
                cv2.imwrite(name, frame)  # 프레임을 'photo0.jpg'에 저장

                face = imageio.imread(name)
                # 암호화
                encrypted = encrypt.kaleidoscope(face, 'pocari sweat', noise=50)
                #암호화 된 사진을 s3에 올리기
                plt.imsave(name, encrypted);  # 암호화된 사진을 로컬에 저장하는 코드

                i += 1
                time = datetime.now()
                print("Number of faces detected: " + str(len(faces)))
                for (x, y, w, h) in faces:
                    print("face location: " + str(x), str(y), str(w), str(h))
                    face_img = frame[y:y + h, x:x + w]  # 인식된 얼굴 이미지 crop
                    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04)  # 축소
                    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)  # 확대
                    frame[y:y + h, x:x + w] = face_img  # 인식된 얼굴 영역 모자이크 처리

        else:
            print('no frame!')
            break

    cv2.imshow('result', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # Esc 키를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()

# 복호화 방법 생각해보기
# getPic = "C:/opencv/photo1.jpg";
# decrypted = encrypt.kaleidoscope(getPic, 'pocari sweat');
# plt.imshow(decrypted)