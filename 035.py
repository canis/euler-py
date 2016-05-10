from utils.math import primes

def rotate(num):
    s = str(num)
    l = len(s)
    rot = set()
    
    for i in range (l):
        s = s[1:] + s[0]
        if num > 9 and int(s[-1]) in [2, 4, 5, 6, 8, 0]:
            return None
        else:
            rot.add(int(s))
    return frozenset(rot)

p = primes(100)
print (p)
r = set()
for num in p:
    rot = rotate(num)
    if rot:
        r.add(rot)

s = len(r)
for fs in r:
    print(fs)
    for num in fs:
        print(num)
        if num not in p:
            print ('---brk')
            s -= 1
            break

print(s)
    


