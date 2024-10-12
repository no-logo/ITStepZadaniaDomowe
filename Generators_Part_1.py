#Zadanie 1
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

