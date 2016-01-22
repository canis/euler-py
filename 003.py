"""
Problem 3
-----------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

from utils.math import primes

n = 600851475143
p = primes(int(n**0.5))
p.reverse()
for i in p:
    if not n%i:
        print(i)
        break
