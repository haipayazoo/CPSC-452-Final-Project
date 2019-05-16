import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host,port))
print("Connected to the server")
message = s.recv(1024)
message = message.decode()
print(message)
while 1:
    message = s.recv(1024)
    message = message.decode()
    print("Server message: ", message)
