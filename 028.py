"""
Problem 28
-----------
Starting with the number 1 and moving to the right in a
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13


It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals
in a 1001 by 1001 spiralformed in the same way?
"""


"""
Explanation

Start: 1
Circle no. 1:  3,  5,  7,  9
Circle no. 2: 13, 17, 21, 25
Circle no. 3: 31, 37, 43, 49
[...]
Let i = "circle number"
and n = 2i that is step in sequence
and m = (n + 1)^2 that is the last element of list
So sum is m + (m - n) + (m - 2n) + (m - 3n)
or 4m - 6n
"""
s = 1
for n in range(2, 1001, 2):
    m = (n + 1)**2
    s += 4*m - 6*n
print (s)
