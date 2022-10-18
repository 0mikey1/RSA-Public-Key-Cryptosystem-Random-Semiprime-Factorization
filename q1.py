import math
import random
import time


def random_prime(n):
    # generates a random n-bit prime number
    if n < 2:
        return -1
    max = 1 << n
    while True:
        r = random.randrange(2, max + 1)
        if primality_test(r, 40):
            return r


def primality_test(n, iterations):
    if ~n & 1 or n == 3:
        if n == 2 or n == 3:
            return True
        else:
            return False
    q = n - 1
    k = 0
    while ~q & 1:
        q >>= 1
        k += 1
    for iteration in range(iterations):
        a = random.randrange(2, n - 1)
        rem = pow(a, q, n)
        if rem == n - 1 or rem == 1:
            continue
        inconclusive = False
        for j in range(1, k):
            rem = pow(rem, 2, n)
            if rem == n - 1:
                inconclusive = True
                break
        if not inconclusive:  # composite
            return False
    return True


def semiprime_factorize(n):
    # precondition: n is a semiprime number: n = p.q
    # returns the ordered pair of prime numbers (p,q)
    # your code is here...
        for i in range (2,int(math.sqrt(n))):
            if n%i==0:
                return(i,n//i)
        return(1,n)

print("Number 21. Prime Factors:   ", semiprime_factorize(21))

print('key length', '\t', 'log(time)')
for nbits in range(32, 65, 2):
    avg_time = 0
    for _ in range(20):
        p = random_prime(nbits >> 1)
        q = random_prime(nbits >> 1)
        t0 = time.time()
        (calculated_p, calculated_q) = semiprime_factorize(p * q)
        elapsed = time.time() - t0
        if (p, q) != (calculated_p, calculated_q) and (p, q) != (calculated_q, calculated_p):
            print("Error: incorrect prime factorization", (p, q), (calculated_p, calculated_q))
        avg_time += elapsed / 20
    if avg_time != 0:
        print(nbits, '\t\t\t', round(math.log10(avg_time) * 100) / 100)