from Crypto.PublicKey import DSA
from Crypto.Hash import SHA512

# Sign the contents of the message
def sign(message, key):
    hash = SHA512.new(message).hexdigest()

    signature = key.sign(hash, 5)
    

    signed_message = message + "," + str(signature[0]) + ',' +str(signature[1])

    return signed_message



# Verify the authenticity of the message
def verify(signature, key, message):
    hash = SHA512.new(message).hexdigest()
    if key.verify(hash, signature):
        print "Authentic"
    else:
        print "Incorrect"


message = "Baboons rule! xDDDD"
key = DSA.generate(1024)
publickey=key.publickey()
y=publickey.keydata[0]
g=publickey.keydata[1]
p=publickey.keydata[2]
q=publickey.keydata[3]
publickey= DSA.construct((long(y),long(g),long(p),long(q)))
message = sign(message, key)
contents = message.rsplit(',', 2)
verifying = verify((long(contents[1]), long(contents[2])), publickey, contents[0])

