import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('182.92.128.53', 12345))
while True:
    msg = 'ccc'
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('recv:', data.decode())
client.close()
