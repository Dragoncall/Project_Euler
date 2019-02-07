import math


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def get_divisors(n):
    return list(divisorGenerator(n))[:-1]


def find_abundant_numbers():
    abundant_numbers = []
    for i in range(1, 28125):
        if i < sum(get_divisors(i)):
            abundant_numbers.append(i)
    return abundant_numbers


def find_sums_of_abundant_numbers():
    abundant_numbers = find_abundant_numbers()
    all_numbers = list(range(0, 28124))
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j < 28124:
                all_numbers[i + j] = 0
    return sum(all_numbers)


if __name__ == '__main__':
    print(find_sums_of_abundant_numbers())
