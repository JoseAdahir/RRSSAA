from math import prod
from secrets import randbelow
import random
from Crypto.Util.number import *
from primefac import primefac
from sympy import *
from sympy.ntheory.modular import crt

def get_prime(n):
    p = 1
    r = random.Random()
    r.seed(randbelow(2**n))
    while not isPrime(p):
        p = r._randbelow(2**256) | 1
    return p

N1 = prod(get_prime(i) for i in range(2, 128))
e = 0x10001
with open("outputRRSSAA.txt") as handle:
    c = handle.read()

c = c.split(" ")
print(c[0])
cipher = bytes.fromhex(c[1][2:])
cipher = bytes_to_long(cipher)
N = bytes.fromhex(c[0][2:])
print(N)
N = bytes_to_long(N)

p = 1
r = random.Random()
primos = []
i=0
while len(primos) < 6:
    r = random.Random()
    p=1
    r.seed(i)
    while not isPrime(p):
        p = r._randbelow(2**256) | 1
    if N % p ==0:
    	while N% p ==0:
            print(p)
            primos.append(p)
            N = N//p
    i+=1
    
print(len(primos))

c_i = []

for p in primos:
    d = inverse(e,p-1)
    c_i.append(pow(cipher,d,p))

plaintext = crt(primos,c_i)
print(plaintext[0])
plaintext = long_to_bytes(plaintext[0])
print(plaintext)


# assert len(flag) == 128
# N = prod(get_prime(i) for i in range(2, len(flag)))
# print(hex(N), hex(pow(bytes_to_long(flag), 0x10001, N)))



