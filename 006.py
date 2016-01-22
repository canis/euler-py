"""
Problem 6
-----------
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares
of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
"""


"""
Danke schön Carl Friedrich Gauß
1 + 2 ... + 100 = 101 * 50 = 5050
"""
sq_of_sum = 5050 ** 2
sum_of_sq = 385 + sum([i**2 for i in range(11, 101)])

print (sq_of_sum - sum_of_sq)
