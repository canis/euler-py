"""
Problem 5
-----------
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

"""
Explanation:

Smallest multiple of primes is it product, then first of all:
i = 2*3*5*7*11*13*17*19
It also divisible by 6 (2*3), 10 (2*5), 14 (2*7) and 15 (3*5)

And we need to find the nearest number which divisible by 4, 8, 9, 12, 16,
18 and 20, so add 2 and 3 to multipliers and get:
i = 2*2*3*3*5*7*11*13*17*19
It also divisible by 4 (2*2), 9 (3*3), 12 (2*2*3), 18 (2*3*3) and 20 (2*2*5)

And now we need to find the nearest number which divisible by 8 and 16
so add 2 and 2 to multipliers and get:
i = 2*2*2*2*3*3*5*7*11*13*17*19
Finally it divisible by 8 (2*2*2) and 16 (2*2*2*2)
"""

i = 2*2*2*2*3*3*5*7*11*13*17*19
print (i)
