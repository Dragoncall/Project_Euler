def prime_factors(number):
    prime_factors = []
    current_number = number
    while current_number != 1:
        for i in range(2, current_number+1):
            if is_prime(i) and current_number % i == 0:
                prime_factors.append(i)
                current_number = current_number//i
                break
    return prime_factors


def is_prime(number):
    for j in range(2, number):
        if number % j == 0:
            return False
    return True



if __name__ == '__main__':
    print(prime_factors(600851475143)[-1])
