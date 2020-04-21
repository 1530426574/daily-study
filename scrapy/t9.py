import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import socket

server = socket.socket()
server.bind(('172.17.8.70', 12345))
server.listen()
conn, addr = server.accept()
print(conn, addr)

data = conn.recv(1024)
print('recive:', data.decode())
conn.send(data.upper())
conn.close()
