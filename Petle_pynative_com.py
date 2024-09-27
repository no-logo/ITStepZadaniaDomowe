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
