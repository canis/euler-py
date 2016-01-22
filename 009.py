"""
Problem 9
-----------
A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Explanation:

Euclid's formula.
m > n, a = m^2 - n^2, b = 2mn, c = m^2 + n^2

so if a + b + c = 1000 then m between sqrt(1000)/2 and sqrt(1000/2)
"""

total = 1000
for m in range(int((total**0.5)//2), int((total/2)**0.5)+1):
    if total % (2 * m) != 0:
        continue
    n = total // (2 * m) - m
    if m > n > 0:
        a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
        print (a * b * c)
        break
