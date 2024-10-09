# Zadanie 1: def add_unique_element(input_list, element): # output: # ['apple', 'banana', 'kiwi', 'orange'] # hint: if not in
print('\nZadanie 1\n')

def add_unique_element(input_list, element):
    result = any(e == element for e in input_list)
    if not result:
        input_list.append(element)
    return input_list

print(add_unique_element(['apple', 'banana', 'kiwi'], 'orange'))
print(add_unique_element(['apple', 'banana', 'kiwi', 'orange'], 'orange'))

#Zadanie 2: def remove_duplicates_and_sort(input_list): # output: # ['apple', 'banana', 'kiwi', 'orange'] # hint: sorted, set
print('\nZadanie 2\n')

def remove_duplicates_and_sort(input_list):
    output_list = list(set(input_list))
    return sorted(output_list)

print(remove_duplicates_and_sort(['orange', 'kiwi', 'banana', 'apple', 'apple', 'banana', 'kiwi', 'orange']))

#Task 1
print('\nTask 1\n')

def product_of_elements(input_list):
    p = 1
    for element in input_list:
        p *= element
    return p

print(product_of_elements([1, 2, 3, 4]))

#Task 2
print('\nTask 2\n')

def minimum_in_list(input_list):
    list_min = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] < list_min:
            list_min = input_list[i]
    return list_min

print(minimum_in_list([1, 2, 3, 4, 0]))

#task 3
print('\nTask 3\n')

def check_prime_numbers(input_list):
    prime_count = 0
    isprime = 1
    for i in input_list:
        if i == 1 or i == 2:
            prime_count += 1
        else:
            for j in range(2, i):
                if i % j == 0:
                    isprime = 0
            prime_count += isprime
        isprime = 1

    return prime_count

print(check_prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

