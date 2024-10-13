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

# Task 2
print('\nTask 2\n')

def sum_of_two_list(l1, l2):
    len_max = max(len(l1), len(l2))

    for r in range(len_max):
        if r >= len(l1):
            l1.append(0)
        if r >= len(l2):
            l2.append(0)

    for r in range(len_max):
        yield l1[r] + l2[r]

l = list(sum_of_two_list([1,2,3,4,5],[1,2]))
print(l)

# Task 3
print('\nTask 3\n')

def square_list_values(list1):
    return [r**2 for r in list1]

def qube_list_values(list1):
    return [r**3 for r in list1]

def calculate(list_to_work, function_to_call):
    return function_to_call(list_to_work)

print(calculate([1,2,3,4], square_list_values))
print(calculate([1,2,3,4], qube_list_values))






