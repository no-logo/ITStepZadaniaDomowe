# Zadanie 1: def print_sentence_multiple_times(): # output: (input = 3) # Hello, Python! # Hello, Python! # Hello, Python!
from scipy.fft import ifftshift

print('\nZadanie 1\n')
def print_sentence_multiple_times(t):
    sentence = '# Hello, Python! '
    print(sentence*t)

print_sentence_multiple_times(3)

#Zadanie 2: def count_upper_lower_chars(input_string): # output: # {'uppercase': 3, 'upper_count': 17, 'other': 7}
print('\nZadanie 2\n')

def count_upper_lower_chars(input_string):
    upper_count = 0
    lower_count = 0
    other_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        if char.islower():
            lower_count += 1
        if  not char.isalpha():
            other_count += 1
    output_dict = {'uppercase' : upper_count, 'upper_count' : lower_count, 'other' : other_count}
    return output_dict

sentence = count_upper_lower_chars('Python Is My Favourite Programming Language')
print(sentence)

#Zadanie 3: def shortest_longest_words(words_list): # output: # ('kiwi', 'grapefruit')
print('\nZadanie 3\n')

def shortest_longest_words(words_list):
     sorted_words_list = sorted(words_list, key=len)
     return sorted_words_list

sorted_list = shortest_longest_words(['grapefruit','kiwi','mango'])
print(sorted_list)

#Task 1
print('\nTask 1\n')

def print_formated_text():
    print('"Don\'t compare yourself with anyone in this world…\nif you do so, you are insulting yourself."\n\t\t\t\t\t\t\t\t\t\t\tBill Gates')

print_formated_text()

#Task 2
print('\nTask 2\n')

def even_numbers(a, b):
    if a % 2 == 0:
        a1 = a
    else:
        a1 = a + 1

    if b % 2 == 0:
        b1 = b + 1
    else:
        b1 = b

    en = list(range(a1, b1,2))
    print(en)

even_numbers(2,9)

#Task 3
print('\nTask 3\n')

def print_square(length, symbol, isSolid):
    if isSolid:
        fsymbol = symbol
    else:
        fsymbol = ' '

    for n in range(length):
        if length == 1:
            print(symbol, end='')
            break
        if length == 2:
            print(symbol*2, end='')
        else:
            if n == 0 or n == length - 1:
                print(symbol*length, end='')
            else:
                print(symbol, end='')
                print(fsymbol*(length-2), end='')
                print(symbol, end='')
        print()

print_square(10,'*',False)
print('\n')
print_square(10,'*',True)


