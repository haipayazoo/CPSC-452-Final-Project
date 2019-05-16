import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host,port))
print("Connected to the server")
message = s.recv(1024)
message = message.decode()
print(message)

message = s.recv(1024)
message = message.decode()
print(message)
            
while True:
    message = s.recv(1024)
    message = message.decode()
    print(message)
    
    new_message = input(str("Client_Two>> "))
    new_message = new_message.encode()
    s.send(new_message)
