import cv2
import numpy as np
from PIL import Image

# 얼굴이 있는 좌표를 받아서 그 좌표가 해당하는 사분면만 따로 저장하기

def crop(imageFile,totalArr):
    print(imageFile)
    img = cv2.imread(imageFile, 0)
    height, width = img.shape

    # 사진 4분의 1 numpy 정의
    a = np.arange(width * height).reshape(height, width)
    print(str(width) + "," + str(height))  # 3024, 4032

    i = 0
    arr = []
    for (x, y, w, h) in totalArr:
        arrays = [(x, y), (x + w, y), (x, y + h), (x + w, y + h)]
        for (first, last) in arrays:
            if first > 0 and first < width // 2:
                if last > 0 and last < height // 2:
                    if 1 not in arr:
                        arr.insert(i, 1)
                        i += 1

            elif first > 0 and first < width // 2:
                if last > 0 and last < height // 2:
                    if 1 not in arr:
                        arr.insert(i, 1)
                        i += 1

            if first > width // 2 and first < width:
                if last > 0 and last < height // 2:
                    if 2 not in arr:
                        arr.insert(i, 2)
                        i += 1
            elif first > width // 2 and first < width:
                if last > 0 and last < height // 2:
                    if 2 not in arr:
                        arr.insert(i, 2)
                        i += 1

            if first > 0 and first < width // 2:
                if last > height // 2 and last < height:
                    if 3 not in arr:
                        arr.insert(i, 3)
                        i += 1

            elif first > 0 and first < width // 2:
                if last > height // 2 and last < height:
                    if 3 not in arr:
                        arr.insert(i, 3)
                        i += 1

            if first > width // 2 and first < width:
                if last > height // 2 and last < height:
                    if 4 not in arr:
                        arr.insert(i, 4)
                        i += 1
            elif first > width // 2 and first < width:
                if last > height // 2 and last < height:
                    if 4 not in arr:
                        arr.insert(i, 4)
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
                    a[j, i + width // 2] = img[j, i + width // 2]
        elif al == 3:
            for j in range(0, height // 2):
                for i in range(0, width // 2):
                    a[j + height // 2, i] = img[j + height // 2, i]
        else:
            for j in range(0, height // 2):
                for i in range(0, width // 2):
                    a[j + height // 2, i + width // 2] = img[j + height // 2, i + width // 2]

    # numpy를 이미지 포맷으로 만들기
    pil_image = Image.fromarray(a)

    # RGB mode가 아니라면 RGB mode로 변경
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')

    splited = imageFile.split('/')
    split_name = splited[len(splited)-1].split('.')
    newFileName = ''
    k = 0
    for i in splited:
        if (k != len(splited) - 1):
            newFileName += i + '/'
            k+=1
    k=0
    for i in split_name:
        if(k != len(split_name)-1):
            newFileName += i + '.'
            k+=1

    newFileName += 'crop.bmp'
    print(newFileName)
    # 4분의 1 영역 저장
    pil_image.save(newFileName, 'BMP')




















