import symmetric_key_lib

print("input something")
tmp = raw_input()

ciphertext = symmetric_key_lib.aes_enc(tmp, b'asdfasdfasdfasdf')
print(ciphertext)

plaintext = symmetric_key_lib.aes_dec(ciphertext, b'asdfasdfasdfasdf')
print(plaintext)