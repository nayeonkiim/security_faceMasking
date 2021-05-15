import numpy as np
import os

# 파일 쓰기
def file_write(filePath, encrypt_data):
    fw = open(filePath, "wb")
    fw.write(encrypt_data)
    n = os.path.getsize(filePath)
    print("file path: " + str(n))
    fw.close()


# 파일 읽기
def file_read(filePath):
    fr = open(filePath, 'rb')
    text = fr.read()
    fr.close()
    # 바이너리 데이터 return
    return text