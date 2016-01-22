"""
Problem 4
-----------
A palindromic number reads the same both ways.
The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

pal = a = b = 0

for i in range(999, 316, -1):
    for j in range(999, i, -1):
        if a > i and b > j:
            break
        result = i*j
        num = str(result)
        if result > pal and num == num[::-1]:
            pal, a, b = result, i, j
            break

print(pal)
