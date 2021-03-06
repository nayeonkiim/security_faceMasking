from camAndEncrypt.encrypt import enc
from camAndEncrypt.img_change import get_img, image_to_byte_array, toImgFile
from camAndEncrypt.file import file_write
from camAndEncrypt.file import file_read
from camAndEncrypt.decrypt import dec
import mysql.connector

# query 실행
def query_executor(cursor, paramMac, paramDatetime):
    sql = "insert into infos(mac, datetime) value(%s,%s)"
    cursor.execute(sql, (paramMac, paramDatetime))


# mySql db 연결
def macInsert(year, month, day, hour, minute, second, mac):

    dateFormat = year + '-' + month + '-' + day + " " + hour + ":" + minute + ":" + second
    print('date : ', dateFormat)

    try:

        mysql_con = mysql.connector.connect(host='localhost', port='3306', database='imgmac', user='root',
                                            password='1234')
        print('db 연결 완료')

        mysql_cursor = mysql_con.cursor(dictionary=True)

        query_executor(mysql_cursor, mac, dateFormat)

        mysql_con.commit()

        for row in mysql_cursor:
            print('mac is: ' + str(row['mac']))

        mysql_cursor.close()


    except Exception as e:
        print(e.message)


    finally:
        if mysql_con is not None:
            mysql_con.close()




def encryptImg(img,path) :
    # 각종 키 정보
    key = bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF])
    aad = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E])
    nonce = bytes([0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC])  # 기본 12(96bit)byte이며 길이 변경 가능.
    plain_data = img # 원본 데이터(바이너리 데이터 넣기)


    # 암호화 시작
    cipher_data, mac = enc(key, aad, nonce, plain_data)
    # 암호화 한 바이너리 데이터 텍스트 파일에 저장하는 경로
    bin_filePath = path + '.bin'
    # 텍스트 파일에 저장
    file_write(bin_filePath, cipher_data)

    return bin_filePath, mac


def decryptImg(bin_filePath, mac, path):
    print(mac)
    # 바이너리 데이터 텍스트 파일에서 읽어오기
    text = file_read(bin_filePath)

    key = bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF])
    aad = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E])
    nonce = bytes([0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC])  # 기본 12(96bit)byte이며 길이 변경 가능.

    # 복호화
    result = dec(key, aad, nonce, text, mac)
    toImgFile(result, path)


















