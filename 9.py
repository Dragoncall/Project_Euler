from math import sqrt, floor


def pythagorean_triplet(number):
    for a in range(1, number):
        for b in range(1, number):
            c = sqrt((a*a) + (b*b))
            if float(c).is_integer() and a+b+c == number:
                return int(a*b*c)



if __name__ == '__main__':
    print(pythagorean_triplet(1000))