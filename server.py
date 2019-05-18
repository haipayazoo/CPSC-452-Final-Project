import socket
from _thread import *

#set up server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ipaddr = '127.0.0.1'
port = 64646

server.bind((ipaddr, port))
server.listen(100)

#this list will contain all active clients
clientList = []

'''
TODO: Fix this authentication function
def user_auth(conn, addr):
		
	user_info = ""
	status = ""

	while status != "success":

		try:
			msg = conn.recv(1024)
			msg = msg.decode()

			credentials = msg.split()		

			file = open("user-pass.txt", "r")

			for info in file:
				user_info = info.split()

				if user_info[0] == credentials[0] and user_info[1] == credentials[1]:
					status = "s"
					print("Credentials confirmed.")
					conn.send(status.encode())
					file.close()
					break

			if(status != "success"):
				print("Did you just print here?")
				conn.send("f".encode())
		
		except:
			continue
'''

#thread_client will be a thread that is running for each client to handled messages
def thread_client(conn, addr):

	#user_auth(conn, addr)

	#welcome the client
	welcomeMsg = "Welcome to Secure Chat!"
	conn.send(welcomeMsg.encode())

	#client main loop
	while True:
		try:
			#try to recieve a message from the client
			msg = conn.recv(1024)

			#if a message has been recieved
			if msg:
				#print the message for debugging
				#TODO: remove this print to because eventually all the traffic will be encrypted
				print(addr[0] + ": " + msg.decode())

				#send the message to all the connected users
				broadcast(msg, conn)
			else:
				#this will handled when the server recieves a weird message. either a disconnect or error
				#regardless we want to disconnect the client
				remove(conn)

		except:
			continue

#broadcast will send a message to all currently connected users except for the one passed as 'conn'
#pass conn=null to broadcast to all
def broadcast(msg, conn):
	#loop through all currently connected clients and send the message
	for client in clientList:

		#if the client is not the one specified to be ignored
		if client != conn:
			try:
				#send the message to the client
				client.send(msg)
			except:
				#if something goes wrong then disconnect the client
				client.close()
				remove(client)

#remove will remove a client from the client list
def remove(conn):
	if conn in clientList:
		clientList.remove(conn)

#the main function of the program
def main():
	print('Starting Server')

	print('Waiting for clients...')
	#our main server loop
	while True:

		#accept a client
		conn, addr = server.accept()

		#add the connection onto the client list in order to make sure the list is always accurate
		clientList.append(conn)

		print(addr[0] + ": connected!", addr)

		#create a new thread for the newly connected client to handled all things related to that clientList
		start_new_thread(thread_client, (conn, addr))


#start the server
main()
conn.close()
server.close()