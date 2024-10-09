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