import numpy as np

# 파일 쓰기


def file_write(filePath, encrypt_data):
    fw = open(filePath, 'wb')
    fw.write(encrypt_data)
    fw.close()


# 파일 읽기
def file_read(filePath):
    fr = open(filePath, 'rb')
    text = fr.read()
    fr.close()
    # 바이너리 데이터 return
    return text