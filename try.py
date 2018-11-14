n = 10
primes = list(range(n))
i = 3
primes[i*i:n:i] = [False]*len(primes[i*i:n:i])
print(primes)