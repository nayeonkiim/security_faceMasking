import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from hyerim.encrypt import enc
from hyerim.file import file_read
from hyerim.img_change import get_img, image_to_byte_array, print_hex_bytes, toImgFile
from middlepresent.decrypt import dec
from middlepresent.file import file_write

image = cv2.imread('C:/opencv/4m20/woman.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

xml = 'C:/Users/hyeri/Desktop/HyeRim/university/Capstone/Security/security_faceMasking/pyFaceEncryption/hyerim/haarcascades/haarcascade_frontalface_default.xml'
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

imageFile='C:/opencv/4m20/woman.bmp'
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

# 4분의 1 영역 저장(잘 잘렸는지 확인하기 위해 저장)
pil_image.save('C:/opencv/4m20/woman_crop.bmp', 'BMP')


# 이미지 파일 가져오기
filePath = 'C:/opencv/4m20/woman_crop.bmp'
img, img_pil = get_img(filePath)

# 각종 키 정보
key = bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF])
aad = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E])
nonce = bytes([0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC])  # 기본 12(96bit)byte이며 길이 변경 가능.
plain_data = image_to_byte_array(img_pil)  # 원본 데이터(바이너리 데이터 넣기)


# 암호화 시작
cipher_data, mac = enc(key, aad, nonce, plain_data)

print('\nEncrypted value:')
# 암호 데이터와 MAC 데이터 출력
print_hex_bytes('\tcipher_data', cipher_data)
print_hex_bytes('\tmac', mac)


# 암호화 한 바이너리 데이터 텍스트 파일에 저장하는 경로
bin_filePath = 'C:/opencv/4m20/ciper.txt'
# 텍스트 파일에 저장
file_write(bin_filePath, cipher_data)


# 암호화 한 바이너리 데이터를 img 형식으로 변환
img_en = toImgFile(cipher_data)
# img(numpy)가 None이기 때문에 사진이 보여지지 않음
cv2.imwrite('C:/opencv/4m20/woman_crop_encrypt.bmp', img_en)


# 바이너리 데이터 텍스트 파일에서 읽어오기
text = file_read(bin_filePath)

# 복호화
result = dec(key, aad, nonce, text, mac)
if result is not None:
    print('\nDecrypted value:')
    print_hex_bytes('\tresult(plain data)', result)


# 암호화 된 바이너리 데이터를 복호화 하여 원본 사진 가져오기
img_de = toImgFile(result)
# 사진 복호화 완료
cv2.imwrite('C:/opencv/4m20/woman_crop_decrypt.bmp', img_de)

#cv2.imshow('sample',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


















