"""
Problem 7
-----------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


"""
See: https://oeis.org/A006880
Precalculated value: range(10**6) contains 78498 prime numbers.
So we can try to use 10 ** 6 as guranteed max value for 
Sieve of Eratosthenes
"""

from utils.math import primes

p = primes(10**6)[10000]
print(p)
