from Crypto.PublicKey import DSA
from Crypto.Hash import SHA512

# Sign the contents of the message
def sign(message, key):
    hash = SHA512.new(message).hexdigest()

    signature = key.sign(hash, key)

    signed_message = message + str(signature[0])

    return signed_message

    

# Verify the authenticity of the message
#def verify():
    

message = "Baboons rule! xDDDD"
key = DSA.generate(1024)
message = sign(message, key)

print(message)