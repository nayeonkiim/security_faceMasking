from datetime import datetime

import os
import cv2
import base64
import threading
from camAndEncrypt.main_img import encryptImg, macInsert


def toencrypt(cap):
    cnt1 = 0
    while (setFlag(cnt1)):
        cnt1 += 1
        # 얼굴 인식
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # 좌우 대칭
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(frame, 1.05, 5)
        print("Number of faces detected: " + str(len(faces)))
        faceArr = []
        for (x, y, w, h) in faces:
            faceArr.append((x, y, w, h))

        i = 0
        time = datetime.now()
        #얼굴 인식된 경우
        if len(faces):
            if ret:
                print("time : " + str(time))
                time2 = datetime.now()
                print("time2 : " + str(time2))  #0.587272 초
                # 시간값도 설정하기
                if (time2-time).seconds >= 15 or i == 0:
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

                    # 초
                    second = str(dt.second)
                    # minute를 05, 08 형태로 만들기
                    if (second.__len__() == 1):
                        second = '0' + second


                    # 사진 캡처된 시간
                    fileName = hour + "." + minute + "." + second
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



def WebcamVieoWriter(cap):
        # 얼굴 인식
        width = int(cap.get(3))
        height = int(cap.get(4))

        fourcc = cv2.VideoWriter_fourcc(*'X264')

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

        file_path = "C:/opencv/" + folderName + "/SaveVideo.mp4"

        # 비디오 저장을 위한 객체를 생성해줌.
        out = cv2.VideoWriter(file_path, fourcc, 5.0, (width, height))

        cnt2 = 0

        while (setFlag(cnt2)):
            cnt2 += 1

            ret, frame = cap.read()

            if not ret:
                print("비디오 읽기 오류")
                break

            frame = cv2.flip(frame, 1)  # 좌우 대칭
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(frame, 1.05, 5)
            print("Number of faces detected: " + str(len(faces)))
            for (x, y, w, h) in faces:
                print(x, y, w, h)
                face_img = frame[y:y + h, x:x + w]  # 인식된 얼굴 이미지 crop
                face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04)  # 축소
                face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)  # 확대
                frame[y:y + h, x:x + w] = face_img  # 인식된 얼굴 영역 모자이크 처리

            # 비디오 프레임이 정확하게 촬영되었으면 화면에 출력하여줌
            cv2.imshow('video', frame)
            # 비디오 프레임이 제대로 출력되면 해당파일에 프레임을 저장
            out.write(frame)

            # ESC키값을 입력받으면 녹화종료 메세지와 함께 녹화종료
            k = cv2.waitKey(1)
            if (k == 27):
                print('녹화 종료')
                break

        # 비디와 관련 장치들을 다 닫아줌.
        cap.release()
        out.release()
        cv2.destroyAllWindows()



# 스레드 종료시키기
def setFlag(cnt) :

    if((mythread2.is_alive() and mythread1.is_alive()) or cnt == 0):
        return True

    else :
        return False



if __name__ == '__main__':
    xml = 'C:/Users/hyeri/Desktop/Capstone/Security/Real-time-face-recognition-and-mosaic-using-deep-learning-master/haarcascades/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(xml)

    cap = cv2.VideoCapture(0)  # 노트북 웹캠을 카메라로 사용
    cap.set(3, 640)  # 너비
    cap.set(4, 480)  # 높이

    mythread1 = threading.Thread(target=toencrypt, args=(cap,))
    mythread2 = threading.Thread(target=WebcamVieoWriter, args=(cap,))

    mythread1.start()
    mythread2.start()


