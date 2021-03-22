import socket
import numpy
import cv2

UDP_IP = "127.0.0.1"
UDP_PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

s = [b'\xff' * 64800 for x in range(96)]

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (1920, 1080))

while True:
    picture = b''

    data, addr = sock.recvfrom(64801)
    s[data[0]] = data[1:64801]

    if data[0] == 95:
        for i in range(96):
            picture += s[i]

        frame = numpy.fromstring(picture, dtype=numpy.uint8)
        frame = frame.reshape(1080, 1920, 3)
        cv2.imshow("frame", frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break