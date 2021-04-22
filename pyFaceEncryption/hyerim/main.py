import binascii

import cv2

from hyerim.decrypt import dec
from hyerim.encrypt import enc
from hyerim.file import file_write, file_read
from hyerim.img_change import get_img, print_hex_bytes, toImgFile, image_to_byte_array

# 이미지 파일 가져오기
filePath = 'C:/opencv/4m20/human2.jpg'
img, img_pil = get_img(filePath)


# 각종 키 정보
key = bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF])
aad = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E])
nonce = bytes([0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC])  # 기본 12(96bit)byte이며 길이 변경 가능.
plain_data = image_to_byte_array(img_pil)  # 원본 데이터(바이너리 데이터 넣기)

# 각각의 키 정보 출력
print_hex_bytes('key', key)
print_hex_bytes('aad', aad)
print_hex_bytes('nonce', nonce)
print_hex_bytes('plain_data', plain_data)

# Header, Data, Tail 부분 찾기 시도
print('plain : ')
#
plain = plain_data.split()
print(type(plain))
plain = plain[1:plain.__sizeof__() - 1]
print(type(plain))
print('plain : ', plain)
data = bytes(plain)
print(type(data))
print('data : ', data)
# print('plain : ', plain[1])


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
cv2.imwrite('C:/opencv/4m20/human3.bmp', img_en)


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
cv2.imwrite('C:/opencv/4m20/human4.bmp', img_de)