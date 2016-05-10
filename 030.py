power = 5
p = [i**power for i in range(10)]

max_digits = 0
for i in range (2, 100):
    if 10**i > p[9]*i:
        max_digits = i
        break

s = 0
for num in range(2, p[9]*max_digits):
    num_s = str(num)
    dig_sum = sum([p[int(a)] for a in num_s])
    if dig_sum == num:
        print (num)
        s += num
print ()
print(s)
