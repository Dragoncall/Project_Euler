def sums_of_3_5(below=1000):
    return sum([i for i in range(below) if i % 3 == 0 or i % 5 == 0])

if __name__ == '__main__':
    print(sums_of_3_5(1000))