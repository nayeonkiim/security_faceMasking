import cv2


imageFile='C:/opencv/4m20/human2.jpg'
img = cv2.imread(imageFile)

# 얼굴 검출을 위한 케스케이드 분류기 생성 ---
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 얼굴 검출 ---④
faces = face_cascade.detectMultiScale(gray)

# 검출된 얼굴 순회 ---⑤
for (x,y,w,h) in faces:
    #검출된 얼굴에 사각형 표시 ---⑥
   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # 얼굴 영역을 ROI로 설정 ---⑦
   roi = gray[y:y+h, x:x+w]


cv2.imshow('sample',img)
cv2.waitKey(0)
cv2.destroyAllWindows()