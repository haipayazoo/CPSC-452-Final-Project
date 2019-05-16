import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print("Starting up CPSC 452 Chat Server...")
print("Waiting for 2 connections...")
client_one, client_one_addr = s.accept()
print("Client one has been connected...")
client_one.send("Welcome to CPSC 452 Chat Server (Client One)".encode())
print("Waiting for 1 connection...")
client_two, client_two_addr = s.accept()
print("Client two has been connected...")
client_two.send("Welcome to CPSC 452 Chat Server (Client 2)".encode())

message = "process...".encode()
client_one.send(message)

while True:
        recv_message = client_one.recv(1024)
        message = "Client One: " + recv_message.decode()
        print("Client One message: ", recv_message.decode())
        client_two.send(message.encode())
        
        recv_message = client_two.recv(1024)
        message = "Client Two: " + recv_message.decode()
        print("Client Two message: ", recv_message.decode())
        client_one.send(message.encode())
