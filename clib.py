import symmetric_key_lib

#takes an algorithm, mode, message, and key
def pro_crypt(alg, mode, msg, key):
	if alg == "AES":
		if mode == "ENC":
			return aes_enc(msg, key)
		else:
			return aes_dec(msg, key)
	else if alg == "RSA":
		if mode == "ENC":
			return b"TODO: implement rsa enc"
		else:
			return b"TODO: implement rsa dec"
	else if alg == "DSA":
		if mode == "ENC":
			return b"TODO: implement dsa enc"
		else
			return b"TODO: implement dsa dec"
