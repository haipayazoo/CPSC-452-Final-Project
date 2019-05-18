from Crypto.PublicKey import DSA
from Crypto.Hash import SHA512

# Sign the contents of the message
def sign(message, key):
    hash = SHA512.new(message).hexdigest()

    signature = key.sign(hash, 5)
    

    signed_message = message + "," + str(signature[0]) + ',' +str(signature[1])

    return signed_message



# Verify the authenticity of the message
def verify(signature, key, hash):
    print(signature[1])
    print(signature[0])
    print hash
    if key.verify(hash, signature):
        print "Authentic"
    else:
        print "Incorrect"


message = "Baboons rule! xDDDD"
key = DSA.generate(1024)
publickey=key.publickey()
message = sign(message, key)
contents = message.rsplit(',', 2)
verifying = verify((long(contents[1]), long(contents[2])), publickey, contents[0])

print(message)
