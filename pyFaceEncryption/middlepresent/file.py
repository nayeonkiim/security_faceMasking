import numpy as np

# 파일 쓰기
from hyerim.img_change import print_hex_bytes


def file_write(filePath, encrypt_data):
    fw = open(filePath, 'wb')
    fw.write(encrypt_data)
    fw.close()


# 파일 읽기
def file_read(filePath):
    fr = open('C:/opencv/4m20/ciper.txt', 'rb')
    text = fr.read()
    fr.close()
    # 바이너리 데이터 return
    return text