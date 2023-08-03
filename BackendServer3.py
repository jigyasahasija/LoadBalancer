import socket
import threading
import time

def thread_func():
    file_path = "www"
    dataRecieved = conn.recv(2048).decode()  ##receives http request data from the socket
    request = dataRecieved.split("\r\n")
    requestStr = "" + request[0]
    requestStr = requestStr.split(' ')
    path = requestStr[1]
    print(path)
    if(path.__eq__("/") or path.__eq__("/index.html")):
        f = open(file_path+"/index3.html","r")
        response =  f"HTTP/1.1 200 OK\r\n\r\n{f.read()}\r\n"
        f.close()
    else:
        response = f"HTTP/1.1 404 Not Found\r\n\r\nNot a valid path: {path}\r\n"
    
    response = bytes(response, 'utf-8')

    print(f"Thread closed for client {address}")
    time.sleep(5)
    conn.send(response)
    conn.close()
    print(f"Connection closed with {address}")

HOST = "127.0.0.3"    ##IP address of our server
PORT= 8002          ##Port number of our server 
threads = []

bs_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bs_obj.bind((HOST,PORT))
bs_obj.settimeout(30)

try:
    while True:
        bs_obj.listen(1)
        print("Waiting for a client")
        conn, address = bs_obj.accept()
        print(f"Connected with {address}")
        conn.settimeout(1)
        th = threading.Thread(target=thread_func,args=())
        threads.append(th)
        th.start()
        print("Out of thread")
except socket.timeout as e:
    print ("Timeout is over")
    print (e)
finally:
    if bs_obj:
        bs_obj.close()
    for t in threads:
        t.join()
        print(f"Thread closing for client {address}")