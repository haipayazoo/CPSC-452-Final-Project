import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host,port))
print("Connected to the server")

# connection been connected message
message = s.recv(1024)
message = message.decode()
print(message)

while True:
    message = s.recv(1024)
    message = message.decode()
    print(message)
    
    new_message = input(str(">> "))
    new_message = new_message.encode()
    s.send(new_message)
