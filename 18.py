input = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def parse_triangle(input):
    return [[int(i) for i in row.split(' ')] for row in input.split('\n')]


def create_empty_triangle(input):
    return [[int(0) for _ in row.split(' ')] for row in input.split('\n')]


def largest_path_in_triangle():
    triangle = parse_triangle(input)
    dp_triangle = create_empty_triangle(input)
    dp_triangle[0][0] = triangle[0][0]
    for i, row in enumerate(triangle[:-1]):
        for j in range(len(triangle[i+1])):
            # We can go to the element beneath or the element to the right
            left = 0
            right = 0
            if j-1 >= 0:
                left = dp_triangle[i][j-1]
            if j < len(triangle[i]):
                right = dp_triangle[i][j]
            dp_triangle[i+1][j] = max(max(right, left) + triangle[i+1][j], dp_triangle[i+1][j])
    return max(dp_triangle[-1])


if __name__ == '__main__':
    print(largest_path_in_triangle())

