#Zadanie 1
print('\nZadanie 1\n')

import string
def shift_characters(input_string):
    alphabet_upper = list(string.ascii_uppercase)
    alphabet_lower = list(string.ascii_lowercase)
    shifted_str = ''

    for letter in input_string:
        if letter in alphabet_upper:
            shifted_str += alphabet_upper[(alphabet_upper.index(letter) + 1) % len(alphabet_upper)]
        elif letter in alphabet_lower:
            shifted_str += alphabet_lower[(alphabet_lower.index(letter) + 1) % len(alphabet_lower)]
        else:
            shifted_str += letter


    return shifted_str

print(shift_characters('String String'))

#Zadanie 2
print('\nZadanie 2\n')

def caesar_cipher(input_string, jump):
    alphabet_upper = list(string.ascii_uppercase)
    alphabet_lower = list(string.ascii_lowercase)
    shifted_str = ''

    for letter in input_string:
        if letter in alphabet_upper:
            shifted_str += alphabet_upper[(alphabet_upper.index(letter) + jump) % len(alphabet_upper)]
        elif letter in alphabet_lower:
            shifted_str += alphabet_lower[(alphabet_lower.index(letter) + jump) % len(alphabet_lower)]
        else:
            shifted_str += letter

    return shifted_str

print(caesar_cipher('String String',10))

# Task 1
print('\nTask 1\n')

def fibonacci_numbers_in_range(begin, end):
    a, b = 0, 1
    for r in range(end + 1):
        if r >= begin:
            yield a
        a, b = b, a + b

print(list(fibonacci_numbers_in_range(3, 12)))






