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


def get_amicable_map(threshold):
    d_map = {}
    for i in range(1, threshold):
        if i not in d_map:
            d_map[i] = []
        d_map[i].append(int(sum(get_divisors(i))))
    return d_map


def sum_of_amicable(threshold):
    d_map = get_amicable_map(threshold)
    result_sum = 0
    used_keys = []
    for key, value in d_map.items():
        if key in used_keys: continue
        for x in value:
            if x != key and x in d_map and key in d_map[x]:
                used_keys.append(x)
                result_sum += key + x
    return result_sum


if __name__ == '__main__':
    print(sum_of_amicable(10000))
