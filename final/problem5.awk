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
	for (g = 2; g <= (p - 1) / 2; ++g) {
#if (g != 5) continue;
		if (gcd(p, g) == 1) coprime = "+"; else coprime = "-"
		printf("%2d%s: ", g, coprime);
		err = 0;
		for (a = 1; a <= (p - 1) / 2; ++a) {
			A = (g ^ a) % p;
			for (b = 1; b <= (p -1) / 2; ++b) {
				B = (g ^ b) % p;
				sA = (B ^ a) % p;
				sB = (A ^ b) % p;
				if (sA != sB) {
					++err;
#					printf("%d-%d--> ", a, b);
#					printf("%d-%d\n", A, B);
				}
				++found[sA];
			}
		}
		n = 0
		for (i = 1; i <= p; ++i) {
			if (i in found) {
				printf("%2d ", found[i]);
				++n;
				delete found[i]
			} else {
				printf("%2d ", 0);
			}			
		}
		printf(" [%2d] --> %d\n", n, err);
	}
}
'


