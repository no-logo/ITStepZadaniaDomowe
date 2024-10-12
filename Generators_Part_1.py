#Zadanie 1
from datetime import time

print('\nZadanie 1\n')

def calculate_word_value(word):
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwyz')

    value = 0

    for letter in word:
        if letter.lower() in vowels:
            value += 3
        elif letter.lower() in consonants:
            value += 1
        elif letter.lower() == 'x':
            value += 10
    return value

print(calculate_word_value('Andrzej xxx Andrzej ====++++'))

#Task 1
print('\nTask 1\n')


def odd_number_in_range(x, y):
    i = x
    while i <= y:
        if i % 2 == 1:
            yield i
        i +=1

print(list(odd_number_in_range(2,13)))

#Task 2
print('\nTask 2\n')

def values_not_in_range(list_of_values, a, b):
    r = range(a, b+1)
    for i in list_of_values:
        if i not in r:
            yield i

print(list(values_not_in_range([1,2,3,4,5,6,7,8,9,10],3,6)))

#Task 3
print('\nTask 3\n')

def vertical_line(symbol):
    l = symbol*10
    for i in l:
        print(i)

def horizontal_line(symbol):
    l = symbol*10
    print(l)

def show_line(symbol, function_to_call):
    function_to_call(symbol)

show_line('#', vertical_line)
show_line('*', horizontal_line)

#Task 4
print('\nTask 4\n')

import time

def time_decorator(func):
    def wrapper():
        start = time.time()
        en = func()
        end = time.time()
        print(en)
        print(f'\nnumber of seconds : {end - start}')
    return wrapper

@time_decorator
def even_numbers():
    even_num = []
    for i in range(100001):
        if i % 2 == 0:
            even_num.append(i)
    return even_num

even_numbers()

#Task 5
print('\nTask 5\n')

def time_decorator1(func):
    def wrapper(a):
        start = time.time()
        en = func(a)
        end = time.time()
        print(en)
        print(f'\nnumber of seconds : {end - start}')
    return wrapper

@time_decorator1
def even_numbers(a):
    even_num = []
    for i in range(a+1):
        if i % 2 == 0:
            even_num.append(i)
    return even_num

even_numbers(1000000)

