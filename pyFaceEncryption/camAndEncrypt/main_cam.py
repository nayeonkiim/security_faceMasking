from datetime import datetime

import os
import cv2
import base64
from camAndEncrypt.main_img import encryptImg, macInsert

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
            if (time2-time).seconds >= 60 or i == 0:
                # 해당 경로에 폴더가 존재하지 않으면 새로 생성
                dt = datetime.now()

                # 월
                month = str(dt.month)
                # month를 05, 08 형태로 만들기
                if (month.__len__() == 1):
                    month = '0' + month

                # 일
                day = str(dt.day)
                # day를 05, 08 형태로 만들기
                if (day.__len__() == 1):
                    day = '0' + day

                folderName = month + "m" + day
                print(folderName)
                path = "C:/opencv/" + folderName

                if not os.path.isdir(path):
                    os.mkdir(path)
                    print('파일 생성 완료')

                # 시
                hour = str(dt.hour)
                # hour를 05, 08 형태로 만들기
                if (hour.__len__() == 1):
                    hour = '0' + hour

                # 분
                minute = str(dt.minute)
                # minute를 05, 08 형태로 만들기
                if (minute.__len__() == 1):
                    minute = '0' + minute

                # 사진 캡처된 시간
                fileName = hour + "." + minute
                print(time)

                name = "C:/opencv/" + folderName + "/" + fileName

                # return : retval(압축 결과 : True / False), img(인코딩된 이미지)
                result, img = cv2.imencode('.bmp', frame, [cv2.IMWRITE_WEBP_QUALITY, 100])
                # 이미지를 base64로 바꾸기
                base64_string = base64.b64encode(img)

                # 사진 암호화(base64 URL)
                x,y = encryptImg(base64_string, name)

                # mac -> String
                macStr = ''

                for idx, c in enumerate(y):
                    macStr += "{:02x}".format(int(c))

                print('macStr : ', macStr)

                # 이미지 mac(y)을 DB에 넣기
                macInsert(str(dt.year), month, day, hour, minute, macStr)

                face = cv2.imread(name)
                i += 1
                time = time2

            else:
                continue;

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



