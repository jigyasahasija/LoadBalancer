import socket

HOST="127.0.0.1"
PORT=1025

socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_obj.bind((HOST,PORT))

print(f"Listening enabled on {(HOST,PORT)}")
socket_obj.listen()
conn, address = socket_obj.accept()
print(f"Connected with {address}")

dataRecieved = conn.recv(2048).decode()  ##receives http request data from the socket
request = dataRecieved.split("\r\n")
requestStr = "" + request[0]
requestStr = requestStr.split(' ')
path = requestStr[1]

response =  b"HTTP/1.1 200 OK\r\n\r\nRespnding from LB\r\n"
conn.send(response)
conn.close()

socket_obj.close()