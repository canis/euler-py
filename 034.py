from math import factorial

f = [factorial(i) for i in range(10)]

max_digits = 0
for i in range (2, 100):
    if 10**i > f[9]*i:
        max_digits = i
        break

s = 0
for num in range(3, f[9]):
    dig_sum = sum(f[int(a)] for a in str(num))
    if dig_sum == num:
        print (num)
        s += num
print ()
print(s)
