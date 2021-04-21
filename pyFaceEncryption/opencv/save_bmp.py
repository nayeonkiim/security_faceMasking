import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

image = cv2.imread('C:/opencv/4m20/two.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

xml = 'C:/Users/rlask/security/Real-time-face-recognition-and-mosaic-using-deep-learning/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)
faces = face_cascade.detectMultiScale(gray, 1.2, 5)

print("Number of faces detected: " + str(len(faces)))

totalArr = []
if len(faces):
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        totalArr.append((x,y,w,h))

print(totalArr)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()

imageFile='C:/opencv/4m20/two.bmp'
img = cv2.imread(imageFile, 0)
height, width = img.shape

# 사진 4분의 1 numpy 정의
a = np.arange(width * height).reshape(height, width)
print(str(width) + "," + str(height))  # 3024, 4032

i=0
arr = []
for (x,y,w,h) in totalArr:
    arrays = [(x,y),(x+w,y),(x,y+h),(x+w,y+h)]
    for (first, last) in arrays :
        if first > 0 and first < width // 2:
            if last > 0 and last < height // 2:
                if 1 not in arr:
                    arr.insert(i,1)
                    i+=1

        elif first > 0 and first < width // 2:
            if last > 0 and last < height // 2:
                if 1 not in arr:
                    arr.insert(i,1)
                    i+=1

        if first > width // 2 and first < width:
            if last > 0 and last < height // 2:
                if 2 not in arr:
                    arr.insert(i,2)
                    i += 1
        elif first > width // 2 and first < width:
            if last > 0 and last < height // 2:
                if 2 not in arr:
                    arr.insert(i,2)
                    i += 1

        if first > 0 and first < width // 2:
            if last > height // 2 and last < height:
                if 3 not in arr:
                    arr.insert(i,3)
                    i += 1

        elif first > 0 and first < width // 2:
            if last > height // 2 and last < height:
                if 3 not in arr:
                    arr.insert(i,3)
                    i += 1

        if first > width // 2 and first < width:
            if last > height // 2 and last < height:
                if 4 not in arr:
                    arr.insert(i,4)
                    i += 1
        elif first > width // 2 and first < width:
            if last > height // 2 and last < height:
                if 4 not in arr:
                    arr.insert(i,4)
                    i += 1

print("arr : " + str(arr))

for al in arr:
    print(al)
    if al == 1:
        for j in range(0, height // 2):
            for i in range(0, width // 2):
                a[j, i] = img[j, i]

    elif al == 2:
        for j in range(0, height // 2):
            for i in range(0, width // 2):
                a[j, i+ width//2] = img[j, i+ width//2]
    elif al == 3:
        for j in range(0, height // 2):
            for i in range(0, width // 2):
                a[j + height//2, i] = img[j + height//2, i]
    else:
        for j in range(0, height // 2):
            for i in range(0, width // 2):
                a[j + height // 2, i + width // 2] = img[j + height // 2, i + width // 2]


# numpy를 이미지 포맷으로 만들기
pil_image=Image.fromarray(a)

# RGB mode가 아니라면 RGB mode로 변경
if pil_image.mode != 'RGB':
    pil_image = pil_image.convert('RGB')

# 4분의 1 영역 저장
pil_image.save('C:/opencv/4m20/na2.bmp', 'BMP')

#cv2.imshow('sample',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



















