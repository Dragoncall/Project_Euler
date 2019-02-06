def sum_of_numbers(numbers):
    return sum(numbers)


def power_of_2(power):
    return sum_of_numbers([int(i) for i in str(1 << power)])

if __name__ == '__main__':
    print(power_of_2(1000))
