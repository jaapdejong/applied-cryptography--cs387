#!/usr/bin/python

# In this assignment, you will write the verify step
# for the bank in the cut-and-choose protocol.  
# 
# The code for the cut-and-choose protocol
# is in the `cutchoose` module
# 1) Alice generates N bills 
# for some amount.
# 2) The bills are sent to the bank.  The bank
# picks one and signs it.
# 3) Before sending it back to Alice, the bank
# asks for the random nonces for the other N-1 bills
# 4) The bank verifies the nonces and the amounts
# before sending back the signed bill
# This last step is where you will be adding your code
#

import cutchoose
from unit6_util import string_to_bits, bits_to_int, pad_to_block, bits_to_string, convert_to_bits, pad_bits

def string_to_int(s):
	return bits_to_int(string_to_bits(s))

def int_to_string(n):
	return bits_to_string(pad_bits(convert_to_bits(n), 8))

def _verify(bills, nonces, value):
    ###########
    ### Your code here
    # Return True if all of the bills
    # have the value specified
    # or False otherwise

# it looks like:
# bills[0..x-1] = "Bill 0. IPBank 50" --> "Bill x-1. IPBank 50"
# ------------- = "Bill x. IPBank 50" (the choosen one)
# bills[x..99]  = "Bill x+1. IPBank 50" --> "Bill 100. IPBank 50"
	nr_bills = len(bills)
#	print "Examining", nr_bills, "bills with", len(nonces), "nonces"
	bill = 0
	for i in range(nr_bills):
#		print "Checking", i, bill
		msg_int = bills[i]
		while bill < nr_bills + 1:
			exp_int = cutchoose.create_bill_message(bill, value, nonces[i])
			if msg_int == exp_int: break
#			print "--> Wrong at bill", bill
			# perhaps next bill matches if the choosen bill is left out at this point
			bill += 1
		bill += 1

	if bill == nr_bills + 1:
#		print "--> OK"
		return True
	else:
#		print "--> FAIL"
		return False
    ###########
    
cutchoose._verify = _verify
def test():
#    print "### Legal ###"
    # Alice generates some bills
    bills = cutchoose.generate_bills(50)
    # and sends them to the bank.
    # The bank picks one and sends
    # back which one
    i = cutchoose.pick_and_sign_bills(bills)
#    print "Choosen bill:", i
    # Alice now needs to send back 
    # the random nonces
    nonces = cutchoose.send_nonces(i)
    # bank checks the nonces and
    # if they pass, returns the signed bill
    signed = cutchoose.verify_bills_and_return_signed(nonces, 50)
    assert signed is not None
    assert bills[i] == pow(signed, cutchoose.BANK_PUBLIC_KEY[0], 
                           cutchoose.BANK_PUBLIC_KEY[1])

    # here, we'll try to cheat and see if we get caught
#    print "### ILLEGAL ###"
    bills = cutchoose.cheat_generate_bills(50, 100)
    i = cutchoose.pick_and_sign_bills(bills)
#    print "Choosen bill:", i
    nonces = cutchoose.send_nonces(i)
    signed = cutchoose.verify_bills_and_return_signed(nonces, 50)
    # there is a 1% chance we got away with this
    assert signed is None

test()
