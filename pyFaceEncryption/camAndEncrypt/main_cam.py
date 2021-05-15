from datetime import datetime

import os
import cv2
import base64
from camAndEncrypt.main_img import encryptImg


xml = '/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)

cap = cv2.VideoCapture(0)  # 노트북 웹캠을 카메라로 사용
cap.set(3, 640)  # 너비
cap.set(4, 480)  # 높이

time = datetime.now()
i = 0
while (True):
    # 얼굴 인식
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # 좌우 대칭
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.05, 5)
    print("Number of faces detected: " + str(len(faces)))
    faceArr = []
    for (x, y, w, h) in faces:
        faceArr.append((x, y, w, h))

    #얼굴 인식된 경우
    if len(faces):
        if ret:
            print("time : " + str(time))
            time2 = datetime.now()
            print("time2 : " + str(time2))  #0.587272 초
            # 시간값도 설정하기
            if (time2-time).microseconds >= 200000 or i == 0:
                if i != 0:
                    time = time2

                # 해당 경로에 폴더가 존재하지 않으면 새로 생성
                dt = datetime.now()
                folderName = str(dt.month) + "m" + str(dt.day)
                print(folderName)
                path = "C:/opencv/" + folderName

                if not os.path.isdir(path):
                    os.mkdir(path)
                    print('파일 생성 완료')

                # 사진 캡처된 시간
                fileName = str(dt.hour) + "." + str(dt.minute) + "." + str(dt.second)
                print(time)

                name = "C:/opencv/" + folderName + "/" + fileName;

                try:
                    # .bmp로 저장
                    cv2.imwrite(name + ".bmp", frame)  # 프레임을 '지금시간'에 저장
                    print('사진 저장 완료')
                except Exception as ex:  # 에러 종류
                    print('사진 업로드 실패', ex)

                #byte 로 변경
                with open(name + ".bmp", 'rb') as img:
                    base64_string = base64.b64encode(img.read())

                # 사진 암호화
                x,y = encryptImg(base64_string, name)

                face = cv2.imread(name)
                i += 1

            else:
                print('no frame!')
                break

        for (x, y, w, h) in faces:
            print(x, y, w, h)
            face_img = frame[y:y + h, x:x + w]  # 인식된 얼굴 이미지 crop
            face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04)  # 축소
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)  # 확대
            frame[y:y + h, x:x + w] = face_img  # 인식된 얼굴 영역 모자이크 처리

            time = datetime.now()

        cv2.imshow('result', frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # Esc 키를 누르면 종료
            break

cap.release()
cv2.destroyAllWindows()



