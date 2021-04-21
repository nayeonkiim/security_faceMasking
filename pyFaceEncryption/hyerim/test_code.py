import base64

import hashlib
import io

import numpy as np
from random import Random
from PIL import Image

import cv2
from Crypto.Cipher import AES


# 이미지 파일 열기
imageFile='C:/opencv/4m20/human2.jpg'
img = cv2.imread(imageFile)
img_pil = Image.open(imageFile)


# 이미지를 바이너리 형태로 바꾸기 1
binary_cv = cv2.imencode('.PNG', img)[1].tobytes()
output = io.BytesIO()
img_pil.save(output, 'PNG')
binary_pil = output.getvalue()
print(type(binary_pil))
print(binary_pil)


# 이미지를 바이너리 형태로 바꾸기 2
def image_to_byte_array(image:Image):
   imgByteArr = io.BytesIO()
   image.save(imgByteArr, format=image.format)
   imgByteArr = imgByteArr.getvalue()
   return imgByteArr

img11 = image_to_byte_array(img_pil)
print(type(img11))



# 바이너리를 numpy 형태로 바꾸기
ArrBin=np.frombuffer(img11, dtype=np.float32)
print(ArrBin)



# numpy를 이미지 포맷으로 만들기
pil_image = Image.fromarray(np.frombuffer(ArrBin, dtype=np.float32))
print(type(pil_image))



# RGB mode가 아니라면 RGB mode로 변경
if pil_image.mode != 'RGB':
    pil_image = pil_image.convert('RGB')



# 이미지 저장
img.save('C:/opencv/4m20/human7.jpg', 'JPEG')
cv2.imwrite('C:/opencv/4m20/human8.jpg', img)




# 이미지를 바이너리 형태로 읽은 후 np.fromstring(data, dtype = np.uint8) 을 하고 그걸 이미지 형태로 변환하기(그래야 이미지가 복원됨 바이너리를 바로 이미지로 바꾸면 이미지가 안나옴)
with open(imageFile, 'rb') as f:
    data = f.read()
print(data)

encoded_img = np.fromstring(data, dtype = np.uint8)
img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

print(type(encoded_img))
print(img)





# 암.복호화
class MyCipher:

    def __init__(self):
        self.BS = 16

        self.pad = lambda s: s + (self.BS - len(s.encode('utf-8')) % self.BS) * chr(
            self.BS - len(s.encode('utf-8')) % self.BS)

        self.unpad = lambda s: s[0:-s[-1]]

        self.key = hashlib.sha256().digest()


    def encrypt(self, raw):
        raw = self.pad(raw)

        iv = Random.new().read(AES.block_size)

        cipher = AES.new(self.key, AES.MODE_CFB, iv)

        return base64.b64encode(iv + cipher.encrypt(raw.encode('utf-8')))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)

        iv = enc[:16]

        cipher = AES.new(self.key, AES.MODE_CFB, iv)

        return self.unpad(cipher.decrypt(enc[16:]))

    def encrypt_str(self, raw):
        return self.encrypt(raw).decode('utf-8')

    def decrypt_str(self, enc):
        if type(enc) == str:
            enc = str.encode(enc)

        return self.decrypt(enc).decode('utf-8')



# 암.복호화 실행
in_str = encoded_img

print(in_str)

in_enc = MyCipher().encrypt(in_str)  # 암호화

print(in_enc)

print("입력된 값: ", MyCipher().decrypt_str(in_enc))  # 복호화