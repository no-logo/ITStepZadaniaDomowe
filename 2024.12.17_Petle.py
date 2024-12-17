#Zadanie 1
liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))

while liczba1 <= liczba2:
    print(liczba1)
    liczba1 += 1

#Zadanie 2
liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))

while liczba1 <= liczba2:
    if liczba1 % 2 == 1:
        print(liczba1)
    liczba1 += 1

#Zadanie 3
liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))

while liczba1 <= liczba2:
    if liczba1 % 2 == 0:
        print(liczba1)
    liczba1 += 1

#Zadanie 4
liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))

while liczba1 <= liczba2:
    print(liczba2)
    liczba2 -= 1

#Zadanie 5
liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))

if liczba2 < liczba1:
    liczba2, liczba1 = liczba1, liczba2

while liczba1 <= liczba2:
    if liczba1 % 2 == 1:
        print(liczba1)
    liczba1 += 1