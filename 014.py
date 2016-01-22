"""
Problem 14
-----------
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

steps_map = {1:1}
max_steps = 0
start_num = 0
for i in range(2, 1000000):
    if i not in steps_map:
        steps = 0
        result = i
        chain = []
        while True:
            result = result*3 + 1 if result%2 else result//2
            steps += 1
            chain.append(result)
            if result in steps_map:
                steps += steps_map[result]
                break
                
        steps_map[i] = steps
        for j in chain:
            steps -= 1
            steps_map[j] = steps
    
    if steps_map[i] > max_steps:
        max_steps = steps_map[i]
        start_num = i


print(max_steps, 'steps for', start_num)


