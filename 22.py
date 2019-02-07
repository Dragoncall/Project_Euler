def read_names(file_name):
    with open(file_name) as f:
        names = f.readline()
        return sorted([name.replace('"', '') for name in names.split('","')])

def calculate_name_score(index, name):
    return sum([ord(char) - ord('A') + 1 for char in name]) * index

if __name__ == '__main__':
    # Small test case from Project Euler
    assert calculate_name_score(938, 'COLIN') == 49714
    print(sum([calculate_name_score(i+1, value) for i, value in enumerate(read_names('./files/p022_names.txt'))]))
