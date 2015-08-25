#!/usr/bin/python

# HW3-5 Version 1

# For this assignment you will be given all of the public information
# of a Diffie-Hellman key exchange plus the number of multiplications
# necessary to calculate (g**b)**a mod p, given g**b where `a` is
# Alice's private key and `b` is Bob's private key
# 
# With this information, you should be able to determine Alice's
# private key and then decrypt the message - which is given at the
# bottom of this file
#
# If you think you've found a bug, post here -
# http://forums.udacity.com/cs387-april2012/questions/2188/hw3-challenge-problem-issues-and-bugs
# For other discussion of the problem, this topic is more appropriate - 
# http://forums.udacity.com/cs387-april2012/questions/2190/hw3-challenge-problem-general-discussion

import string

#############
# p and g are public information
#

# 2 ** 100 - 153 is prime 
# (from http://primes.utm.edu/lists/2small/0bit.html) 
# and verified using Wolfram Alpha
p = 1267650600228229401496703205223 

# primitive root (calculated using wolfram alpha)
g = 3

#############
# g_a, g_b are both transmitted public
#  and easily intercepted by a passive eavesdropper
#
# g_a = g**a mod p
# g_b = g**b mod p
 
g_a = 142621255265782287951127214876
g_b = 609743693736442153553407144551

#############
# Unfortunately, for Alice, she is using a modular
# exponentiation function similar to the one discussed
# in lecture and we were able to count the number of
# multiplications used to calculate the key

n_multiplications = 26

############################
# This eliminates the recursion in the mod_exp
# shown in lecture
# and does bitwise operations
# to speed things up a bit
# but the number of multiplications stays
# the same
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

# `count_multiplications` might be useful
# to see if you've found an exponent that
# would require the same number multiplications
# as Alice's private key
def count_multiplications(exponent):
    """return the number of multiplications
    necessary to raise a number to `exponent`"""
    bits = convert_to_bits(exponent)
    return len(bits) + sum(b for b in bits) - 2

# this is the encode function used to 
# create the cipher text found at the bottom of the file
def encode(plaintext, key):
    assert len(plaintext) <= len(key)
    return [m^k for m, k in zip(plaintext, key)]

# use this function to decrypt the ciphertext
def decode(ciphertext, key):
    assert len(ciphertext) <= len(key)
    return [c^k for c,k in zip(ciphertext, key)]

# is_valid returns True if the input consist of valid
# characters (numbers, upper case A-Z and lower case a-z and space)
# The message still might be garbage, but this is a decent
# and reasonably fast preliminary filter
valid_chars = set(c for c in string.printable[:62])
valid_chars.add(' ')
def is_valid(decode_guess):
    return (len(decode_guess) == 14 and 
            all(d in valid_chars for d in decode_guess))

# Below are the typical bit manipulation functions
# that you might find useful
# Note that ASCII_BITS is set to 7 for this problem

BITS = ('0', '1')
ASCII_BITS = 7 

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
        result = [(n % 2)] + result
        n = n / 2
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

############
# `ciphertext` is the observed message exchanged between Alice
# and Bob - which is what you need to decrypt
#
# key = convert_to_bits(mod_exp(g_b, a, p))
# ciphertext = encode(string_to_bits(plaintext), key)

ciphertext = string_to_bits(' x\x0br\x1fu/W\x00gJ@h#')

###########
# `plaintext` is the variable you will need to set
# with the decrypted message

plaintext = "" # Your answer here 

###########
###########
###########
#
# Alice
#	g_a = g^a mod p
#	send g, p & g_a
#
# Bob
#	g_b = g^b mod p
#	send g_b
#	key = g_a^b mod p
#
# Alice
#	key = g_b^a mod p
#	n_multiplications (NrOfMultiplications to calculate Alice's Key)
#	send cyphertext
#
# I know
#	g = 3
#	p = 1267650600228229401496703205223
#	g_a = 142621255265782287951127214876
#	g_b = 609743693736442153553407144551
#	cyphertext = string_to_bits(' x\x0br\x1fu/W\x00gJ@h#') (14 chars)
#	n_multiplications = 26
#	mod_exp(g_b, a, p)
#		a & 1 == 0 - 1 multiplication
#		a & 1 == 1 - 2 multiplications needed
#
# I don't know
#	a
#	b
#	key
#	plaintext = decode(cyphertext, key)
#
#	key = 609743693736442153553407144551^a mod 1267650600228229401496703205223
#	for a in range():
#		if multiplications(a) == n_multiplications:
#			# we have a candidate
#			key = mod_exp(g_b, a, p)
#			print decode(cyphertext, key)
#		
#
#
###########
###########
###########



# Might be a useful test function.
# If you've calculated Alice's key
# and the plaintext, you can
# calculate a cipher-text to see
# if it matches the given `ciphertext`
def test(alices_key, plaintext):
    key = convert_to_bits(mod_exp(g_b, alices_key, p))
    test_cipher = encode(string_to_bits(plaintext), key)
    return test_cipher == ciphertext

### uncomment to run
#print test(alices_key, plaintext)

for a in range(1, 100000000):
    if count_multiplications(a) == n_multiplications:
        key = convert_to_bits(mod_exp(g_b, a, p))
        if len(key) >= len(ciphertext):
            plaintext = bits_to_string(decode(ciphertext, key))
            if is_valid(plaintext):
                print "a = ", a, " plaintext = |", plaintext, "|"



###
### a =  119765  plaintext = | zTv q6B34x tWq |
### a =  129764  plaintext = | jpk7DDGCXt6jax |
### a =  188823  plaintext = | jGMyUJ4shdMees |
### a =  203605  plaintext = | htvfd9pz0d2fxw |
### a =  308425  plaintext = | wYAF7HmHnpUclb |
### a =  350761  plaintext = | C3OTsUz7WVzobr |
### a =  476679  plaintext = | R0fuqi5SeeLKVf |
### a =  536686  plaintext = | FWI1T4KSVCCZAP |
### a =  1442416  plaintext = | momOYiJQeIzjNP |
### a =  2396674  plaintext = | FgleFHLXLTPBUo |
### a =  6301760  plaintext = | attack at dawn | <<<===
### 
