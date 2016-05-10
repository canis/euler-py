def primes(n):
    primes = []
    multiples = set()
    for i in range(1, n+1, 2):
        if i == 1:
            i = 2
        if i not in multiples:
            primes.append(i)
            if i*i < n+1:
                multiples.update(range(i*i, n+1, i))

    return primes
    
def divisors(num, primes, with_self=True, with_one=True):
    n = num
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n > 1:
        factors.append((n, 1))

    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]

    if not with_one:
        div.remove(1)
    if not with_self:
        div.remove(num)

    div.sort()
    
    return div
