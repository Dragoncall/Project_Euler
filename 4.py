def largest_palindrome_product(amount_of_digits=3):
    max_value = int('9' * amount_of_digits)
    palindromes = set()
    for i in range(1, max_value + 1):
        for j in range(1, max_value + 1):
            if is_palindrome(i * j):
                palindromes.add(i * j)
    return max(palindromes)


def is_palindrome(number):
    number_string = str(number)
    for i, decimal in enumerate(number_string):
        if number_string[i] != number_string[len(number_string) - i - 1]:
            return False
    return True


if __name__ == '__main__':
    print(largest_palindrome_product(amount_of_digits=3))
