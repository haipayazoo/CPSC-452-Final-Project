import socket
from clib import *

class Connection():

	def __init__(self, addr, port, asmAlgo):
		self.addr = addr
		self.port = port
		self.asmKey = None
		self.symKey = None

	def sendUnencrypted(self, message):
		# TODO

	def sendAsymmetric(self, algorithm, message):
		# TODO

	def sendSymmetric(self, message):
		# TODO

	def send(self, message):
		# TODO

	def receive(self):
		# TODO

	def close(self):
		# TODO
