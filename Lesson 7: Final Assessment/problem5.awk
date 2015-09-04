#!/bin/sh

# Alice and Bob agree to use a modulus p = 23 and base g = 5 (which is a primitive root modulo 23).
# Alice chooses a secret integer a = 6, then sends Bob A = ga mod p
#	A = 56 mod 23 = 8
# Bob chooses a secret integer b = 15, then sends Alice B = gb mod p
#	B = 515 mod 23 = 19
# Alice computes s = Ba mod p
#	s = 196 mod 23 = 2
# Bob computes s = Ab mod p
#	s = 815 mod 23 = 2
# Alice and Bob now share a secret (the number 2).

awk '
function gcd(p, q)
{
	while (q) {
		t = p; 
		p = q; 
		q = t % q;
	}
	return p < 0 ? -p : p;
}

BEGIN {
	p = 23;
	for (g = 2; g <= (p - 1) / 2; ++g) {			# step through all possible g values
#if (g != 5) continue;
		coprime = gcd(p, g) == 1 ? "+" : "-";		# p and g relative prime?
		printf("%2d%s: ", g, coprime);
		nkeys = 0
		nerrs = 0;
		for (a = 1; a <= (p - 1) / 2; ++a) {		# step through all possible values Alice could choose
			A = (g ^ a) % p;			# Alices value to be sent to Bob
			for (b = 1; b <= (p -1) / 2; ++b) {	# step through all possible values Bob could choose
				B = (g ^ b) % p;		# Bobs value to be sent to Alice
				sA = (B ^ a) % p;		# the key Alice calculates
				sB = (A ^ b) % p;		# the key Bob calculates
				if (sA != sB) {			# they should be equal!
					++errs;
#					printf("%d-%d-->%d-%d\n ", a, b, A, B);
				}
				if (! (sA in found)) ++nkeys;
				++found[sA];			# add the found key
			}
		}
		for (i = 1; i <= p; ++i) {
			if (i in found) {
				printf("%2d ", found[i]);
#				++nkeys;
				delete found[i]
			} else {
				printf("%2d ", 0);
			}			
		}
		# show nr of different keys and nr of times Alice and Bob calculate a different key
		printf(" [%2d] --> %d\n", nkeys, nerrs);
	}
	exit
}
'


