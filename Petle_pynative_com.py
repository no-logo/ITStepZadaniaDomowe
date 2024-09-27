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