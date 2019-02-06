import math


def generate_triangle_numbers():
    x = 0
    previous_max = 0
    while True:
        x += 1
        previous_max = previous_max + x
        yield previous_max


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def get_triangle_number_with_divisors(amount_of_divisors):
    for number in generate_triangle_numbers():
        if len(list(divisorGenerator(number))) >= amount_of_divisors:
            return number

if __name__ == '__main__':
    print(get_triangle_number_with_divisors(500))