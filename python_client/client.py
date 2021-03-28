import socket
import time
import sys

TAG_IMAGE_FILE = 'a.txt'

UDP_IP = "218.51.138.245"
UDP_PORT = 40000
buf = 1024

file_name = 'C:/Users/hyeri/Desktop/' + TAG_IMAGE_FILE
print('file_name', file_name)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
net_filename = file_name.encode()
sock.sendto(net_filename, (UDP_IP, UDP_PORT))
print("Sending {} ...".format(file_name))

f = open(file_name, "rb")
data = f.read(buf)
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close()
f.close()
