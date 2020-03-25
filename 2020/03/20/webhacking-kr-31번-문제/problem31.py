import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("소켓 생성성공")
except socket.error as err :
    print("error : %s"%(err))

host = '210.217.38.14'
port = 9999

s.bind((host,port))
s.listen(5)
print("%d 포트 연결 대기중"%(port))

while True:
    client, addr = s.accept()
    print(addr, "접속")
    flag = client.recv(1024).decode()
    print("msg : "+flag)
    client.close()