def sum_of_squares(max):
    return sum([i * i for i in range(1, max + 1)])

def square_of_sum(max):
    x = sum([i for i in range(1, max + 1)])
    return x*x

if __name__ == '__main__':
    print(square_of_sum(100) - sum_of_squares(100))