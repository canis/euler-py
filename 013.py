"""
Problem 13
-----------
Work out the first ten digits of the sum of
the following one-hundred 50-digit numbers.

[moved to data/013.txt]

"""
with open('data/013.txt', 'rt') as f:
    numbers = [int(s.strip()) for s in f]
    print (str(sum(numbers))[0:10])
f.closed
