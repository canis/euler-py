"""
Problem 11
-----------
In the 20×20 grid below, four numbers along a diagonal line
have been marked in red.

[moved to data/011.txt]

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbersin the same
direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

with open('data/011.txt', 'rt') as f:
    lines = [s.strip() for s in f]
    grid = [line.split(' ') for line in lines]
    grid = [[int(num) for num in line] for line in grid]
f.closed

max_prod = 0
for y in range(17):
    for x in range(17):
        prod = max(
            grid[y][x]   * grid[y][x+1]   * grid[y][x+2]   * grid[y][x+3],
            grid[y][x]   * grid[y+1][x]   * grid[y+2][x]   * grid[y+3][x],
            grid[y][x]   * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3],
            grid[y][x+3] * grid[y+1][x+2] * grid[y+2][x+1] * grid[y+3][x]
        )
        if prod > max_prod:
            max_prod = prod
                
print(max_prod)

    

