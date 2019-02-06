import itertools
from math import sqrt, ceil


def prime_sieve(n):
    plane = [i for i in range(2, n)]
    for i, value in enumerate([i for i in range(2, ceil(sqrt(n)))]):
        if value not in plane:
            continue
        for j, plane_value in enumerate(plane):
            if plane_value != value and plane_value % value == 0:
                plane[j] = 0
        plane = [i for i in plane if i != 0]
    return sum(plane)


if __name__ == '__main__':
    print(prime_sieve(2000000))
