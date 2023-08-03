import socket
import threading
import time

def thread_func(i):
    # Choose a server to forward the connection to
        server_sock.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        server_sock[i].connect(("localhost", servers[i]))
        print(i)
        # Forward the connection
        server_sock[i].sendall(client_sock.recv(1024))
        client_sock.sendall(server_sock[i].recv(1024))

        print(f"Thread for client {client_addr}")
        time.sleep(5)
        # Close the connections
        client_sock.close()
        server_sock[i].close()
        print(f"Connection closed with {client_addr}")

HOST = "127.0.0.1"
PORT = 1025
threads = []
servers = [8000,8001,8002]
i = 0
server_sock = []
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
        client_sock.settimeout(1)
        th = threading.Thread(target=thread_func,args=(i,))
        threads.append(th)
        i=(i+1)%3
        th.start()
except socket.timeout as e:
    print ("Timeout is over")
    print (e)
finally:
    if lb_obj:
        lb_obj.close()
    for t in threads:
        t.join()
        print(f"Thread closing for client {client_addr}")