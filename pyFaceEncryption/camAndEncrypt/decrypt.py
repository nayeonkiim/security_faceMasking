from Cryptodome.Cipher import AES


# 바이트 어레이 표시함수(확인 끝나면 없애도 될 듯)
def print_hex_bytes(name, byte_array):
    print('{} len[{}]: '.format(name, len(byte_array)), end='')
    for idx, c in enumerate(byte_array):
        print("{:02x}".format(int(c)), end='')
    print("")


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
        print('exit dec function ---------------------------------')
        print(type(plain_data))
        # 복호화 된 값 리턴
        return plain_data

    except ValueError:
        # MAC Tag가 틀리다면, 즉, 훼손된 데이터
        print ("Key incorrect")
        print('exit dec function ---------------------------------')
        # 복호화 실패
        return None