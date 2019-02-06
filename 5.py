from functools import reduce

def new_divisor(number, divisors):
    current_number = number
    for divisor in divisors:
        if current_number % divisor == 0:
            current_number = current_number//divisor
    return current_number


def even_divisible(max_number):
    divisors = []
    for i in range(1, max_number+1):
        divisors.append(new_divisor(i, divisors))
    return reduce(lambda x, y: x * y, divisors)


if __name__ == '__main__':
    print(even_divisible(20))