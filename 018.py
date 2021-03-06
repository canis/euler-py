"""
Problem 18
-----------
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

[moved to data/018.txt]

NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge
with a triangle containing one-hundred rows; it cannot be solved
by brute force, and requires a clever method! ;o)
"""

with open('data/018.txt', 'rt') as f:
    grid = [line.split(' ') for line in [s.strip() for s in f]]
    grid.reverse()
    grid = [[int(num) for num in line] for line in grid]
f.closed

for r in range(0, len(grid)):
    row = grid[r]
    for c in range(1, len(row)):
        grid[r+1][c-1] += max(row[c], row[c-1])

print (grid[-1][-1])

        
    
