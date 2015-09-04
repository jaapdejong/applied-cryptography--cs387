#!/usr/bin/python

# HW3-4 Version 1
# 
# Implement the Rabin Miller test for primality
#

from random import randrange

def mod_exp(a, b, q):
    y = 1
    while b > 1:
        if b & 1 == 1: y *= a % q
        b >>= 1
        a *= a % q
    return a * y % q

def rabin_miller(n, target=128):
    """returns True if prob(`n` is composite) <= 2**(-`target`)"""
    ###############
    ## Start your code here
    if n < 2: return False
    if n < 4: return True
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(target):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    ## End of your code
    ###############

def test():
    for i in range(2, 128):
        if rabin_miller(i): print i

test()


