from functools import reduce


def factorials(n):
    return reduce(lambda x, y: x * y, [i for i in range(1, n)])


if __name__ == '__main__':
    print(sum([int(i) for i in str(factorials(100))]))
