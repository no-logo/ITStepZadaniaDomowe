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

#Zadanie 1
liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))

if liczba2 < liczba1:
    liczba2, liczba1 = liczba1, liczba2

suma_liczb = 0

while liczba1 <= liczba2:
    suma_liczb += liczba1
    liczba1 += 1

srednia_liczb = suma_liczb / (liczba2 - liczba1 +1)

print(f'Suma liczb to {srednia_liczb}')
print(f'Średnia liczb to {srednia_liczb}')

#Zadanie 2
liczba1 = int(input('Podaj pierwszą liczbę: '))

iloczyn = 1

while 0 < liczba1:
    iloczyn *= liczba1
    liczba1 -= 1

print(f'{liczba1}! = {iloczyn}')

#Zadanie 3
dl_linii = int(input('Podaj dlugosc linii: '))
print('*'*dl_linii)

#Zadanie 4
dl_linii = int(input('Podaj dlugosc linii: '))
symbol = input('Podaj symbol: ')
print(symbol*dl_linii)

