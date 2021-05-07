import io

import cv2
from PIL import Image
import numpy as np



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
def toImgFile(cipher_data, path):
    encoded_img = np.fromstring(cipher_data, dtype=np.uint8)
    print("encoded_img: " + str(type(encoded_img)))

    array = np.reshape(encoded_img, (480, 640, 3))

    data = Image.fromarray(array)
    data.save(path + ".jpg");



