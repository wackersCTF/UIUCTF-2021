# back_to_basics uiuctf 2021 crypto
'''
Shoutout to those people who think that base64 is proper encryption

author: epistemologist
'''
from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary
#from secret import flag, key

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

def base_n_encode(bytes_in, base):
        return mpz(bytes_to_long(bytes_in)).digits(base).upper().encode()

def base_n_decode(bytes_in, base):
        bytes_out = to_binary(mpz(bytes_in))[:1:-1]
        #        bytes_out = to_binary(mpz(bytes_in, base=base))[:1:-1]

        return bytes_out

def encrypt(bytes_in, key):
        out = bytes_in #FLAG
        for i in key:
                print(i)
                out = base_n_encode(out, ALPHABET.index(i)) # index where i is found in ALPHABET is used as the base
        return out

def decrypt(bytes_in, key):
        out = bytes_in
        for i in key:
                out = base_n_decode(out, ALPHABET.index(i))
        return out

"""
flag_enc = encrypt(flag, key)
f = open("flag_enc", "wb")
f.write(flag_enc)
f.close()
"""
f = open("flag_enc","rb")
f = str(f.read())

print(ALPHABET.index(b"#"))

for i in range(37): # indices go from 0 to 36
        try:
                x = base_n_decode(f,i)
                print(x)

        except:
                print("failed on " + str(i))
