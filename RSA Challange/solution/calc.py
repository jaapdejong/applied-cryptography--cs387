#!/usr/bin/python

e = 65537

from fractions import gcd

def calcD(totient, e):
	u0 = 1
	d = 0
	u2 = totient
	v0 = 0
	v1 = 1
	v2 = e
	while v2 != 0:
		q = u2 / v2
		t0 = u0 - q * v0
		t1 = d - q * v1
		t2 = u2 - q * v2
		u0 = v0
		d = v1
		u2 = v2
		v0 = t0
		v1 = t1
		v2 = t2

	if d < 0: d = d + totient
	assert (e * d) % totient == 1
	return d

import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64

def pempriv(n, e, d, p, q, dP, dQ, qInv):
	template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
	seq = pyasn1.type.univ.Sequence()
	for x in [0, n, e, d, p, q, dP, dQ, qInv]:
		seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
	der = pyasn1.codec.der.encoder.encode(seq)
	return template.format(base64.encodestring(der).decode('ascii'))

from Crypto.PublicKey import RSA

KEYS = 100
n = []
for i in range(0, KEYS):
	fileName = '../challenge/%03d.pem' % (i + 1);
	pem = open(fileName).read()
	N = RSA.importKey(pem).n
	n.append(N)

for i in range(0, KEYS):
	for j in range(0, KEYS):
		if i == j: continue
		
		p = gcd(n[i], n[j])
		if p == 1: continue

		print "Public key", i + 1, " shares a factor with", j + 1

		q = n[i] // p
		totient = (p - 1) * (q - 1) 
		d = calcD(totient, e)
		dP = d % (p - 1)
		dQ = d % (q - 1)
		qInv = pow(q, p - 2, p)

		fileName = 'privatekey-%03d.pem' % (i + 1);
		f = open(fileName, 'w')
		f.write(pempriv(n[i], e, d, p, q, dP, dQ, qInv))
		f.close()

