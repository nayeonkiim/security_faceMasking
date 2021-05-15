
from Cryptodome.Cipher import AES

# 바이트 어레이 표시함수(확인 끝나면 없애도 될 듯)
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
    #print_hex_bytes('cipher_data', cipher_data)
    print_hex_bytes('mac', mac)
    print('exit enc function ---------------------------------')
    # 암호 데이터와 mac 리턴
    return cipher_data, mac