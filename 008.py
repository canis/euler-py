"""
Problem 8
-----------
The four adjacent digits in the 1000-digit number
that have the greatest product are 9 × 9 × 8 × 9 = 5832.

[moved to data/008.txt]

Find the thirteen adjacent digits in the 1000-digit number
that have the greatest product. What is the value of this product?
"""


with open('data/008.txt', 'rt') as f:
    numbers = [int(i) for i in ''.join([s.strip() for s in f])]
f.closed

seq = 13
max_prod = 0

for i in range(len(numbers) - seq):

    cut = numbers[i:i+seq]
    
    if 0 in cut:
        continue

    prod = 1
    for n in cut:
        prod *= n

    if prod > max_prod:
        max_prod = prod

print (max_prod)
