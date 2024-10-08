# Zadanie 1: def print_sentence_multiple_times(): # output: (input = 3) # Hello, Python! # Hello, Python! # Hello, Python!
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

