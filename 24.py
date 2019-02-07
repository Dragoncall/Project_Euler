from math import factorial


def millionth_permutation():
    useable_characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 1000000 - 1
    current_sequence = []
    while len(useable_characters) > 1:
        # We know that each digit contributes for the amount of factorial(useable_characters - 1)
        # We can thus divide x by that amount and see how much is left to see which number we should take next
        next_number = (x // (factorial(len(useable_characters) - 1))) % len(useable_characters)
        current_sequence.append(useable_characters.pop(next_number))
    # Add the last character to the current_sequence
    return current_sequence + useable_characters


if __name__ == '__main__':
    print(millionth_permutation())
