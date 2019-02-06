def fibonaci(max=1):
    x1 = 1
    x2 = 1
    y = 1
    while y < max:
        y = x1 + x2
        yield y
        x1 = x2
        x2 = y


if __name__ == '__main__':
    print(sum([i for i in fibonaci(4000000) if i % 2 == 0]))
