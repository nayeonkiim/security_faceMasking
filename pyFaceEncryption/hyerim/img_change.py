import io

import cv2
from PIL import Image
import numpy as np


# 바이트 어레이 표시함수(확인 끝나면 없애도 될 듯)
def print_hex_bytes(name, byte_array):
    print('{} len[{}]: '.format(name, len(byte_array)), end='')
    for idx, c in enumerate(byte_array):
        print("{:02x}".format(int(c)), end='')
    print("")


# 이미지 가져오기
def get_img(filePath):
    img = cv2.imread(filePath)  # cv2로 가져오기
    img_pil = Image.open(filePath)  # Image로 가져오기

    # cv2, Image 형식으로 img return
    return img, img_pil



# 이미지를 바이너리 형태로 바꾸기
def image_to_byte_array(image: Image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    # 바이너리 데이터 return
    return imgByteArr



# 바이너리 데이터를 img 형식으로 변환
def toImgFile(cipher_data):
    encoded_img = np.fromstring(cipher_data, dtype=np.uint8)
    img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    # 이미지 파일 return
    return img

