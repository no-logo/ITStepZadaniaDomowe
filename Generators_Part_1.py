#Zadanie 1
print('\nZadanie 1')

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
print('\nTask 1')


def odd_number_in_range(x, y):
    i = x
    while i <= y:
        if i % 2 == 1:
            yield i
        i +=1

print(list(odd_number_in_range(2,13)))