#!/usr/bin/python

#!/usr/bin/python

# HW3-2 Version 1
#
# Define a procedure primitive_roots 
# that takes as input a small prime number
# and returns all the primitive roots of that number
#

def mod_exp(a, b, q):
    y = 1
    while b > 1:
        if b & 1 == 1: y *= a % q
        b >>= 1
        a *= a % q
    return a * y % q

def primitive_roots(n):
    """Returns all the primitive_roots of 'n'"""
    roots = []
    ##########
    # Start of your code
    for r in range(2, n):
        s = set()
        for i in range(2, n):
            t = mod_exp(r, i, n)
            if t in s: break
            if i == n - 1: roots.append(r)
            s.add(t)
    print n, " --> ", roots
    return roots
    #  End of your code
    ##########

def test():
    assert primitive_roots(3) == [2]
    assert primitive_roots(5) == [2, 3]
    assert primitive_roots(7) == [3, 5]
    assert primitive_roots(11) == [2, 6, 7, 8]
    assert primitive_roots(13) == [2, 6, 7, 11]
    assert primitive_roots(17) == [3, 5, 6, 7, 10, 11, 12, 14]
    assert primitive_roots(19) == [2, 3, 10, 13, 14, 15]
    assert primitive_roots(23) == [5, 7, 10, 11, 14, 15, 17, 19, 20, 21]
    assert primitive_roots(29) == [2, 3, 8, 10, 11, 14, 15, 18, 19, 21, 26, 27]
    assert primitive_roots(31) == [3, 11, 12, 13, 17, 21, 22, 24]

    print "tests pass"

test()
#primitive_roots(7)

