import socket
from clib import *

class Connection():

	#connection constructor
	# - addr - the ip address to use
	# - port - the port to use
	# - isServer - set to true if this is the connection to listen on and false if it is a client connection
	def __init__(self, addr, port, isServer):
		self.addr = addr
		self.port = port
		self.isServer = isServer

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		if self.isServer:
			#if this connection is a server we need to bind the port and listen for connections
			self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.sock.bind((self.addr, self.port))
			self.sock.listen(100)
		else:
			#if this connection is a client we need to connect to the server
			self.sock.connect((self.addr, self.port))

	def __init__(self, sock):
		self.isServer = False
		self.sock = sock;

	def sendUnencrypted(self, message):
		self.sock.send(message)

	def sendAsymmetric(self, algorithm, message):
		# TODO
		self.sock.send(algorithm + encrypt(algorithm, message, self.asmKey))

	def sendSymmetric(self, message):
		# TODO
		self.sock.send(A_AES + encrypt(A_AES, message, self.symKey))

	def receive(self):
		# TODO
		msg_raw = self.sock.recv(1024)





	def close(self):
		# TODO

	#accepts a socket connection if this connection is a server
	def accept(self):
		if isServer:
			return self.sock.accept()
		else:
			return False
