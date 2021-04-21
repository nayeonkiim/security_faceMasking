import io

import cv2
from Cryptodome.Cipher import AES
from PIL import Image

import numpy as np

# 이미지 가져오기
imageFile='C:/opencv/4m20/human2.jpg'
img = cv2.imread(imageFile) # cv2로 가져오기
img_pil = Image.open(imageFile) # Image로 가져오기


# 이미지를 바이너리 형태로 바꾸기
binary_cv = cv2.imencode('.JPEG', img)[1].tobytes()
output = io.BytesIO()
img_pil.save(output, 'JPEG')
binary_pil = output.getvalue()



# 바이트 어레이 표시함수
def print_hex_bytes(name, byte_array):
    print('{} len[{}]: '.format(name, len(byte_array)), end='')
    for idx, c in enumerate(byte_array):
        print("{:02x}".format(int(c)), end='')
    print("")


# 암호화 함수
def enc(key, aad, nonce, plain_data):
    print('\nenter enc function ---------------------------------')
    # AES GCM으로 암호화 라이브러리 생성
    cipher = AES.new(key, AES.MODE_GCM, nonce)

    # aad(Associated Data) 추가
    cipher.update(aad)

    # 암호!!!
    cipher_data = cipher.encrypt(plain_data)
    mac = cipher.digest()

    # 암호화된 데이터 와 MAC Tag(Message Authentication Codes tag) 출력
    print_hex_bytes('cipher_data', cipher_data)
    print_hex_bytes('mac', mac)
    print('exit enc function ---------------------------------')
    # 암호 데이터와 mac 리턴
    return cipher_data, mac


# 복호화 함수
def dec(key, aad, nonce, cipher_data, mac):
    print('\nenter dec function ---------------------------------')
    # 암호화 라이브러리 생성
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    # aad(Associated Data) 추가
    cipher.update(aad)

    try:
        # 복호화!!!
        plain_data = cipher.decrypt_and_verify(cipher_data, mac)
        # 암호화된 데이터 출력
        print_hex_bytes('plain_data', plain_data)
        print('exit dec function ---------------------------------')
        # 복호화 된 값 리턴
        return plain_data

    except ValueError:
        # MAC Tag가 틀리다면, 즉, 훼손된 데이터
        print ("Key incorrect")
        print('exit dec function ---------------------------------')
        # 복호화 실패
        return None


if __name__ == "__main__":
    # 각종 키 정보
    key = bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF])
    aad = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E])  #
    nonce = bytes(
        [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC])  # 기본 12(96bit)byte이며 길이 변경 가능.
    plain_data = binary_pil  # 원본 데이터(바이너리 데이터 넣기)

    # 각각의 키 정보 출력
    print_hex_bytes('key', key)
    print_hex_bytes('aad', aad)
    print_hex_bytes('nonce', nonce)
    print_hex_bytes('plain_data', plain_data)


    # 암호화 시작
    cipher_data, mac = enc(key, aad, nonce, plain_data)

    print('\nEncrypted value:')
    # 암호 데이터와 MAC 데이터 출력
    print_hex_bytes('\tcipher_data', cipher_data)
    print_hex_bytes('\tmac', mac)

    # 암호화 한 바이너리 데이터를 img 형식으로 변환
    encoded_img = np.fromstring(cipher_data, dtype=np.uint8)
    print(encoded_img)
    img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    print(img)
    # img(numpy)가 None이기 때문에 사진이 보여지지 않음
    cv2.imwrite('C:/opencv/4m20/human8.jpg', img)


    # 복호화
    result = dec(key, aad, nonce, cipher_data, mac)
    if result is not None:
        print('\nDecrypted value:')
        print_hex_bytes('\tresult(plain data)', result)

    # 암호화 된 바이너리 데이터를 복호화 하여 원본 사진 가져오기
    decoded_img = np.fromstring(result, dtype=np.uint8)
    print(decoded_img)
    img = cv2.imdecode(decoded_img, cv2.IMREAD_COLOR)
    print(img)
    # 사진 복호화 완료
    cv2.imwrite('C:/opencv/4m20/human9.jpg', img)





