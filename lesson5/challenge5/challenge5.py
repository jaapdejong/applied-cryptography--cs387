#!/usr/bin/python

# HW5 Challenge Problem 5 

# For this problem, we've attempted to make a
# simplified example demonstrating the beast
# attack.  We've created a simple site
# that has a secret message, `m`.

# You have the ability to send a message, attack, to 
# the server.  The server will prepend
# `attack` to `m` and then encrypt the resulting
# message using CBC mode with a block size
# of 128 bits.  

# The initialization vector, iv, is used from
# the the last block of the last encryption.
# Dave outlined how to deal with and use 
# this in lecture.  He also discussed a paper
# by Thai Duong and Juliano Rizzo that might
# have more useful information

# Specifically, the code below POSTs two values
# `attack` and `token`.  `attack` is the string
# prepended to the message and `token` is used
# internally to maintain a session and keep track
# of the last `iv.`  We highly recommend you don't
# mess with it.
# If `token` is empty or invalid - the server generates a
# random iv value and uses that for the encryption

# Rarely, similar to how a user might close and start
# a new TLS session, the server will start over, pick a new random
# IV and use that for encryption.

# The send function takes in a string as an argument and returns
# a string as an argument.  This is different from previous
# assignments where most functions took in arrays of bits.
# Just remember that each character represents a byte (8 bits)

# More information available: http://forums.udacity.com/cs387-april2012/questions/3506/hw5-5-challenge-question-discussion

###################
# This code is provided as an example of how to send and recieve
# information from the server.
# 
# You should only need to use the `send` function

import urllib
import json
import base64

BLOCK_SIZE = 128
site = "http://cs387.udacity-extras.appspot.com/beast"

def unencode_json(txt):
	d = json.loads(txt)
	return dict((str(k),
		base64.urlsafe_b64decode(str(v)))
		for k,v in d.iteritems())

def _send(attack=None, token=None):
	data = {}
	if attack is not None:
		data["attack"] = base64.urlsafe_b64encode(attack)
	if token is not None:
		data["token"] = base64.urlsafe_b64encode(token)

	# here we make a post request to the server, sending
	# the attack and token data
	json = urllib.urlopen(site, urllib.urlencode(data)).read()
	json = unencode_json(json)
	return json
    
_TOKEN = None
def send(attack=None):
	"""send takes a string (representing bytes) as an argument 
	and returns a string (also, representing bytes)"""
	global _TOKEN
	json = _send(attack, _TOKEN)
	_TOKEN = json["token"]
	return json["message"]

# End of example code
##################

##################
# Change secret_message to be the decrypted value
# from the server

BITS = ('0', '1')
ASCII_BITS = 8

### bits_to_*
def bits_to_char(b):
	assert len(b) <= ASCII_BITS
	value = 0
	for e in b:
		value = (value * 2) + e
	return chr(value)

def bits_to_string(b):
	return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
					for i in range(0, len(b), ASCII_BITS)])

def bits_to_int(b):
	value = 0
	for e in b:
		value = (value * 2) + e
	return value

### string_to_*
def string_to_int(s):
	return bits_to_int(string_to_bits(s))
	
def pad_bits(bits, pad):
	"""pads seq with leading 0s up to length pad"""
	assert len(bits) <= pad
	return [0] * (pad - len(bits)) + bits

def string_to_bits(s):
	def chr_to_bit(c):
		return pad_bits(int_to_bits(ord(c)), ASCII_BITS)
	return [b for group in 
			map(chr_to_bit, s)
			for b in group]

### int_to_*
def int_to_bits(n):
	result = []
	if n == 0:
		return [0]
	while n > 0:
		result = [n % 2] + result
		n = n / 2
	while len(result) % ASCII_BITS != 0:
		result = [0] + result
	return result

def int_to_string(n):
	return bits_to_string(int_to_bits(n))

### other stuff
def xor(a, b):
	assert len(a) == len(b)
	return [aa^bb for aa, bb in zip(a, b)]

from string import printable
valid_chars = set(c for c in printable)
valid_chars.add(' ')
def isValid(decode_guess):
	return all(d in valid_chars for d in decode_guess)

# string to hex
def toHex(s):
	lst = []
	for ch in s:
		hv = hex(ord(ch)).replace('0x', '')
		if len(hv) == 1:
			hv = '0'+hv
		lst.append(hv)
    
	return reduce(lambda x,y:x+y, lst)

# hex to string
from string import atoi
def toStr(s):
	return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''

# an attacker observing 2 consecutive ciphertext blocks C0, C1
# can test if the plaintext block P1 is equal to x by choosing
# the next plaintext block P2 = x ^ C0 ^ C1; due to how CBC
# works C2 will be equal to C1 if x = P1.
from string import printable
valid_chars = set(c for c in printable)
valid_chars.add(' ')

BLOCK_SIZE_BYTES = BLOCK_SIZE / ASCII_BITS

def sendRecv(attack):
	b = string_to_bits(send(attack))
	blocks = []
	# split into blocks
	for i in range(len(b) / BLOCK_SIZE):
		blocks.append(b[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE])
	return blocks

def zeros(bytes):
	return [0 for i in range(bytes * ASCII_BITS)]

def length():
	blocks = sendRecv(None)
	nr_blocks = len(blocks)
	nr_chars = nr_blocks * BLOCK_SIZE_BYTES
	for i in range(BLOCK_SIZE_BYTES):
		# i == 0 - zero_bits is 15 bytes long
		# i == 1 - zero_bits is 14 bytes long
		# ...
		zero_bits = zeros(BLOCK_SIZE_BYTES - 1 - i)

		blocks = sendRecv(bits_to_string(zero_bits))

		# if nr of block received now is the same as with the empty message, we stripped the 
		# padding of the original message
		if len(blocks) == nr_blocks:
			break
			
	return nr_chars, nr_chars - BLOCK_SIZE_BYTES + i

def decode(secret = '', check = False):
	start_char = len(secret)
	for i in range(start_char, nr_chars_message):
	
		if len(secret) != i:
			print "Not good..."
			return None
			
		# i ==  0 / 16 / 32 - zero_bits is 15 bytes long
		# i ==  1 / 17 / 33 - zero_bits is 14 bytes long
		# ...
		# i == 15 / 31 / 47 - zero_bits is 0 bytes long
		nr_zero_chars = (nr_chars - 1 - i) % BLOCK_SIZE_BYTES
		zero_bits = zeros(nr_zero_chars)
		zero_string = bits_to_string(zero_bits)
			
		# i ==  0 / 16 / 32 - send 15 bytes + orig message
		# i ==  1 / 17 / 33 - send 14 bytes + orig message
		# ...
		# i == 15 / 31 / 47 - send 0 bytes + orig message
		blocksA = sendRecv(zero_string)
		
		# send it again
		blocksB = blocks = sendRecv(zero_string)
		
		# what block to use as IV0
		verify = i // BLOCK_SIZE_BYTES
		if verify == 0: IV0_bits = blocksA[-1]
		else: IV0_bits = blocksB[verify - 1]
		
		# now find the next char 'brute force'
		newch = '#'
		for ch in valid_chars:

			# last block previous message
			IV1_bits = blocks[-1]	# i = 0..15

			# i ==  0 / 16 / 32 - send 15 bytes + ?
			# i ==  1 / 17 / 33 - send 14 bytes + ch1 + ?
			# ...
			# i == 15 / 31 / 47 - send 0 bytes + ch1 + ch2 ... + ch15 + ?
			bits = zero_bits + string_to_bits(secret) + int_to_bits(ord(ch))
			bits = xor(xor(IV0_bits, IV1_bits), bits[-BLOCK_SIZE:])
			
			# send it
			blocks = sendRecv(bits_to_string(bits))
			
			# match?
			if blocks[0] == blocksB[verify]:
				newch = ch
				break

		secret += newch
		print "<", secret, ">"
		if check: return

# determine length
nr_chars, nr_chars_message = length()
print "Expecting", nr_chars_message, "characters in a message with", nr_chars, "characters"

# test run (spaces are detected early)
#decode('What hath God', True)
#decode('What hath God wrought?', True)
#decode('What hath God wrought? -Samuel', True)

# full run (takes 4 to 5 minutes to complete)
decode()

# and this is the outcome
secret_message = 'What hath God wrought? -Samuel Morse'


