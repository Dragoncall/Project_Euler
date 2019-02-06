import itertools


def prime_sieve(n):
    current_primes = []
    for value in itertools.count():
        prime = (value >= 2)

        for j in current_primes:
            if value % j == 0:
                prime = False

        if prime:
            current_primes.append(value)
            print(len(current_primes))

            if len(current_primes) == n:
                return current_primes[-1]


if __name__ == '__main__':
    print(prime_sieve(10001))
