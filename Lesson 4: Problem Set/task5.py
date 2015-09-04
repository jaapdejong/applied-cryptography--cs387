#!/usr/bin/python

# HW4-05 Version 1
#
# Use RSA and OAEP padding to decrypt the ciphertext below
# Put your answer in the plaintext variable

from hashlib import sha512

BITS = ('0', '1')
ASCII_BITS = 8

def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits
        
def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        if n % 2:
            value = 1
        else:
            value = 0
        result = [value] + result
        n = n / 2
    while len(result) % ASCII_BITS != 0:
        result = [0] + result
        
    return result

def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
                    for i in range(0, len(b), ASCII_BITS)])

def bits_to_int(b):
    value = 0
    for e in b:
        value = (value * 2) + e
    return value

def mod_exp(a, b, q):
    """return a**b % q"""
    val = 1
    mult = a
    while b > 0:
        odd = b & 1 # bitwise and
        if odd == 1:
            val = (val * mult) % q
            b -= 1
        if b == 0:
            break
        mult = (mult * mult) % q
        b = b >> 1 # bitwise divide by 2
    return val

# private key
n = 163337384206254196136256905164215818685586918951141221126394408668809777452520349668859723974634222518738526976760766017511678181884780117277802125689306872778510779111021304067611411071215920387754683047176920988231245806047339117003013267749350166593203943400463471064009273107286997981419079779353871913613L

d = 72306394717363424299328399722663981135942256932885379363091911199772788859003622146161074079559455936549462817183931881228142994229843306261555995399517375703257594404049732148740472823878934537674252191478702048647471522520082576645795404386769847966042578016616602577622451300338631726401289028172301100673L

# public key
e = 65537

# variables used in padding
g = 512
h = 512

def hash(input_, length):
    h = sha512(bits_to_string(input_)).digest()
    return string_to_bits(h)[:length]

def xor(a, b):
    assert len(a) == len(b)
    return [aa^bb for aa, bb in zip(a, b)]

def oaep_pad(message, nonce, g, h):
    mm = message + [0] * (g - len(message))
    G = xor(mm, hash(nonce, g))
    H = xor(nonce, hash(G, h))
    return G + H
    
def encrypt(message, n, public_key, nonce, g, h):
    oaep = oaep_pad(message, nonce, g, h)
    m_int = bits_to_int(oaep)
    return convert_to_bits(pow(m_int, public_key, n))

##################
# ciphertext was created by calling
# `encrypt` where message and nonce are secret

ciphertext = string_to_bits("\x98WRQ5\xf4\xe5L$a\xf4\xbf\xecV\\\xb1\xe4\x18\xf1It\x01\xca\xdc\xd0@\xc8\xf6\x97\xf9K\xb8\x1b\x9a\x17\x89\xa9\xcap\x9a\xb5\xb4\x12\xf6\x01\x9avd\xedc*\xcbELRi\xf7.?\x82H\xd3Ci\xd7\xaea7\xbc\x00+\xf04\x13>\xe6q\xf3\xedg\xc4VWB\x8a\x9f\xdf%-8\xf3\x08\xc59\x84\xec\xf8G\xbe\xd2Ub\xf9K4\xa0\xa4(\xeaI\x19T\x1fM\xa6+\x81\xb0\x8d\x04\x99<%o3C-\xc6")


# pad
#    mm = message + [0] * (g - len(message))
#    G = xor(mm, hash(nonce, g))
#    H = xor(nonce, hash(G, h))
#    PlainMessage = G + H

# unpad



plaintext = "" # YOUR ANSWER HERE

def decrypt(message, n, private_key):
    m_int = bits_to_int(message)
    plain_int = mod_exp(m_int, private_key, n)
    # unpad
    # G = eerste 512 bytes
    # H = tweede 512 bytes
    s = convert_to_bits(plain_int)
    G = s[0:g]
    H = s[g:g+h]
    r = xor(H, hash(G, h))
    m0 = xor(G, hash(r, g))
    return bits_to_string(m0)


assert bits_to_int([1, 0, 1, 0]) == 10
print "|", decrypt(ciphertext, n, d), "|"

