"""
Problem 21
-----------
Let d(n) be defined as the sum of proper divisors of
n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from utils.math import *

min_n = 220
max_n = 10000
primes = primes(int(max_n**0.5))
nums = [n for n in range(min_n, max_n+1) if n not in primes]
pairs = dict()
amics_sum = 0

for num in nums:
    divs = sum(divisors(num, primes, with_self=False))
    if divs in pairs and pairs[divs] == num:
        amics_sum += num + divs
    else:
        pairs[num] = divs
print (amics_sum)
