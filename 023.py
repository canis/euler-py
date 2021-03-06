"""
Problem 23
-----------
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
"""

from utils.math import *

max_num = 28123
min_num = 12
p = primes(max_num)
ab = []
"""
# Find all abundant numbers in 2..28123
for i in range(2, max_num):
    if i in p:
        continue
    d = divisors(i, p, with_self=False)
    if i >= sum(d):
        continue
    ab.append(i)

cbw = list(range(1, max_num))

# Find all numbers which cannot be written...
for i in ab:
    for j in ab:
        try:
            cbw.remove(i + j)
        except ValueError:
            pass

print (cbw)
""" 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    for j in a:
        print (i, j, i+j)
    print ("rem" + str(i))
    a.remove(i)

