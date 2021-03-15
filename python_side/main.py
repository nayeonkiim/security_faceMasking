import socket
import threading
import time


def current_milli_time():
    return round(time.time() * 1000)


# 서버의 주소입니다. hostname 또는 ip address를 사용할 수 있습니다.
HOST = '218.51.138.245'
# 서버에서 지정해 놓은 포트 번호입니다. 
PORT = 40000

# 파이썬 클라이언트에서 자바랑 연동을 해서 그걸 자바에서 직렬화를 해서 소켓 통신을 하는 건 가능할 듯!
# 그래서 그렇게 직렬화된 파일을 자바로 전송한다는 개념!
#픽셀 정보는 3차원 Matrix이기 때문에. Matrix를 전송하려면 어떤 파일에 담아서 전송을 해야 하는데
#그 전송을 할 매개체를 어떻게 할 거냐는 문제인거지.


# 소켓 객체를 생성합니다. 
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다. 
client_socket.connect((HOST, PORT))

# 10번의 루프로 send receive를 한다.
for i in range(1,10):
    # 메시지를 보낸다.
    msg = str(current_milli_time())
    # 메시지를 바이너리(byte)형식으로 변환한다.
    data = msg.encode()
    # 메시지 길이를 구한다.
    length = len(data)
    # server로 little 엔디언 형식으로 데이터 길이를 전송한다.
    client_socket.sendall(length.to_bytes(4, byteorder="little"))
    # 데이터를 전송한다.
    client_socket.sendall(data)
    # server로 부터 전송받을 데이터 길이를 받는다.
    data = client_socket.recv(4)
    # 데이터 길이는 little 엔디언 형식으로 int를 변환한다.
    length = int.from_bytes(data, "big")
    # 데이터 길이를 받는다.
    data = client_socket.recv(length)
    # 데이터를 수신한다.
    msg = data.decode()
    # 데이터를 출력한다.
    print('Received from : ', msg)
client_socket.close()

# reference: https://nowonbun.tistory.com/672
