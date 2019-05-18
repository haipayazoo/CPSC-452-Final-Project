import base64
from Crypto.Cipher import AES
from Crypto import Random

#takes an algorithm, mode, message, and key
def encrypt(alg, msg, key):
	if alg == "AES":
		return aes_enc(msg, key)
	else if alg == "RSA":
		return b"TODO: implement rsa enc"
	else if alg == "DSA":
		return b"TODO: implement dsa enc"

def decrypt(alg, msg, key):
	if alg == "AES":
		return aes_dec(msg, key)
	else if alg == "RSA":
		return b"TODO: implement rsa dec"
	else if alg == "DSA":
		return b"TODO: implement dsa dec"

def aes_enc(msg, key):

	#create an initialization vector
	iv = Random.new().read(AES.block_size)

	#create the cipher and encrypt
	cipher = AES.new(key, AES.MODE_CFB, iv)
	ciphertext = iv + cipher.encrypt(msg)

	#base 64 encode and return
	return base64.b64encode(ciphertext)

def aes_dec(msg, key):

	#decode the msg into raw format
	raw = base64.b64decode(msg)

	#get the initialization vector off the front of the message
	iv = raw[:AES.block_size]

	#set up the cipher and decrypt
	cipher = AES.new(key, AES.MODE_CFB, iv)
	return cipher.decrypt(raw[AES.block_size:])
