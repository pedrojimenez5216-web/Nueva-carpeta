def suma_primos(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    return sum(i for i, prime in enumerate(sieve) if prime)

print(suma_primos(2000000))
