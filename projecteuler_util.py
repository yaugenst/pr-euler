from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if (n == 2) or (n == 3):
        return True
    if (n%2 == 0) or (n%3 == 0):
        return False
    i = 5
    w = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += w
        w = 6 - 4
    return True

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def factorial(n):
    if (n == 1) or (n == 0):
        return 1
    return n*(factorial(n - 1))

def binomial(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def proper_divisors(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t) + 1):
        if n % i == 0:
            s += i + n/i
    if t == int(t):
        s -= t
    return s

def memoize(f):
    cache = {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf
