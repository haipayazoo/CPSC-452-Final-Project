import socket
from _thread import *

#initialize client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddr = '127.0.0.1'
port = 64646

#connect to the server
sock.connect((ipaddr, port))

#thread_socket is a thread that will handled all traffic from the socket
def thread_socket():

	#thread main loop
	while True:
		try:
			#try to recieve a message from the server
			msg = sock.recv(1024)

			#if a message has been recieved
			if msg:
				#print the message
				print(msg.decode())

		except:
			continue

#variabled
running = True

while running:

	#initialize the recieving loop
	start_new_thread(thread_socket, ())

	#main loop for listening to client inputs
	while True:

		#get the input from the user
		msg = input()

		#send the message to the server
		if msg:
			sock.send(msg.encode())

sock.close()