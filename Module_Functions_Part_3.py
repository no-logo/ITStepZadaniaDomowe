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

