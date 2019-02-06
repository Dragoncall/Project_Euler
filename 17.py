sinle_digit = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
digit_ten = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 9, 19: 8}
digit_single = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
td = {0: 10, 1: 13, 2: 13, 3: 15, 4: 14, 5: 14, 6: 13, 7: 15, 8: 15, 9: 14}
cd = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7,
      17: 9, 18: 8, 19: 8}


def cw(n):
    if n < 10:
        return sinle_digit[n % 10]
    elif n < 100:
        if n < 20:
            return digit_ten[n]
        else:
            return digit_single[int(n / 10)] + sinle_digit[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return sinle_digit[int(n / 100)] + 7
        elif n % 100 < 20:
            return td[int(n / 100)] + cd[n % 100]
        else:
            return td[int(n / 100)] + digit_single[(n % 100) // 10] + sinle_digit[n % 10]


if __name__ == '__main__':
    count = 0
    for i in range(1, 1000):
        count = count + cw(i)
    print(count + 10)
