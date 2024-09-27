#Exercise 1: Print first 10 natural numbers using while loop
print('\nExercise 1\n')
i = 1
while i <= 10:
    print(i)
    i += 1


#Exercise 2: Print the following pattern
print('\nExercise 2\n')
i = 1
while i <= 5:
    for j in range(1, i+1):
        print(j, end=' ')
    print('')
    i += 1

#Exercise 3: Calculate sum of all numbers from 1 to a given number
print('\nExercise 3\n')

a = int(input('Podaj liczbę a: '))
suma = 0
for s in range(1, a+1):
    suma += s
print(f'suma liczb od 1 do a = {suma}')

#Exercise 4: Print multiplication table of a given number
print('\nExercise 4\n')

a = int(input('Podaj liczbę a: '))
for r in range(1, 11):
    print(a*r)

#Exercise 5: Display numbers from a list using a loop
print('\nExercise 5\n')

numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n > 500:
        break
    if n % 5 ==0 and n <= 150:
        print(n)

#Exercise 6: Count the total number of digits in a number
print('\nExercise 6\n')

a = int(input('Podaj liczbę a: '))
d = 1
number_of_digits = 0

while abs(a/d) >= 1:
    number_of_digits += 1
    d *= 10
print(number_of_digits)

#Exercise 7: Print the following pattern
print('\nExercise 7\n')

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print('')

#Exercise 8: Print list in reverse order using a loop
print('\nExercise 8\n')

list1 = [10, 20, 30, 40, 50]

for n in range(len(list1)-1, -1, -1):
    print(list1[n])