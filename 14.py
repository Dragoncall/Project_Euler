def collatz_serie(start):
    current = start
    while current != 1:
        yield current
        if current % 2 == 0:
            current = current/2
        else:
            current = 3 * current + 1


def longest_serie(max):
    longest_serie = 1
    longest_length = 0
    for i in range(1,max):
        serie = list(collatz_serie(i))
        if len(serie) > longest_length:
            longest_length = len(serie)
            longest_serie = i
    return longest_serie


if __name__ == '__main__':
    print(longest_serie(1000000))