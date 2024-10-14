# Zadanie 1
print('\nZadanie 1\n')
def second_occurrence_index(input_list, element):
    first = input_list.index(element)
    second = input_list.index(element, first + 1)
    return second

print(second_occurrence_index(['apple','banana','orange','banana','plum'],'banana'))

# Zadanie 2
print('\nZadanie 2\n')

def sort_non_negative_numbers(input_list):
    non_negative_numbers = [i for i in input_list if i >= 0]
    return sorted(non_negative_numbers)

print(sort_non_negative_numbers([5, -3, 0, 9, -2, 7, -1, 4]))

# Task 1
print('\nTask 1\n')

def find_greatest_common_divisor(a, b, d = 0):
    if a > b:
        a, b = b, a
    if a % (a-d) == 0 and b % (a-d) == 0:
        return d
    else:
        d += 1
        return find_greatest_common_divisor(a, b, d)

print(find_greatest_common_divisor(8,12))

# Task 2
print('\nTask 2\n')

import random
def bulls_and_cows(n, a = 1):
    g = input('Guess four-digit number: ')

    if g == n:
        return a
    else:
        bools = 0
        cows = 0
        for i in range(4):
            if g[i] in n:
                bools += 1
            if g[i] == n[i]:
                cows += 1
        print(f'bools = {bools}, cows = {cows}')
        a += 1
        return bulls_and_cows(n, a)


numbers = (random.sample(range(10), 4))
number = ''.join([str(x) for x in numbers])
print(bulls_and_cows(number))
print(f'my number was: {number}')
