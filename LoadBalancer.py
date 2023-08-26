import socket
import time
import sys

HOST = "127.0.0.1"
PORT = 1025
servers = [8000,8001,8002]
i = 0
n=sys.argv[1]

lb_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lb_obj.bind((HOST,PORT))
lb_obj.settimeout(30)
print(f"Listening enabled on {(HOST,PORT)}")

try:
    while True:
        lb_obj.listen(5)
        # Accept an incoming connection
        client_sock, client_addr = lb_obj.accept()
        print("Received connection from", client_addr)
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.connect(("0.0.0.0", servers[i]))
        server_sock.sendall(client_sock.recv(1024))
        client_sock.sendall(server_sock.recv(1024))
        i=(i+1)%int(n)
        client_sock.close()
        server_sock.close()
        print(f"Connection closed with {client_addr}")
except socket.timeout as e:
    print ("Timeout is over")
    print (e)
finally:
    if lb_obj:
        lb_obj.close()