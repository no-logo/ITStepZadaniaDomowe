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

#Exercise 9: Display numbers from -10 to -1 using for loop
print('\nExercise 9\n')

for r in range(-10,0):
    print(r)

#Exercise 10: Display a message “Done” after the successful execution of the for loop
print('\nExercise 10\n')

for i in range(5):
    print(i)
else:
    print('Done!')

#Exercise 11: Print all prime numbers within a range
print('\nExercise 11\n')

start = 25
end = 50

p = 0

for n in range(start,end+1):
    for i in range(n,0,-1):
        if n % i == 0:
            p += 1
    if p == 2:
        print(n)
    p = 0

#Exercise 12: Display Fibonacci series up to 10 terms
print('\nExercise 12\n')

print('Fibonacci sequence:')
fib = [0,1]
for n in range(1,11):
    fib.append(fib[n]+fib[n-1])
    print(fib[n-1],end = ' ')

#Exercise 13: Find the factorial of a given number
print('\nExercise 13\n')

a = int(input('Podaj liczbę a: '))

f = 1

for r in range(a,0,-1):
    f *= r
print(f)

#Exercise 14: Reverse a integer number
print('\nExercise 14\n')

n = 76542
s = ''

for r in range(len(str(n)) -1, -1, -1):
    s += str(n)[r]
print(s)

#Exercise 15: Print elements from a given list present at odd index positions
print('\nExercise 15\n')
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for r in range(1,len(my_list),2):
    print(my_list[r], end = ' ')
