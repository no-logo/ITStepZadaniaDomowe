#zadanie 1
ilosc_sekund_od_poczatku_dnia = int(input('Podaj ilość sekund jakie upłynęły od początku dnia: '))
ilosc_sekund_do_konca_dnia = 86400 - ilosc_sekund_od_poczatku_dnia
ilosc_godzin = ilosc_sekund_do_konca_dnia // 3600
ilosc_minut = (ilosc_sekund_do_konca_dnia - (ilosc_godzin * 3600)) // 60
ilosc_sekund = ilosc_sekund_do_konca_dnia - (ilosc_godzin * 3600) - (ilosc_minut * 60)
print(f'Do północy zostało : {ilosc_godzin} godzin {ilosc_minut} minut i {ilosc_sekund} sekund')

#zadanie 2
from math import pi
srednica_okregu = float(input('Podaj srednica okregu: '))

print('Co mam obliczyć:')
print('1 pole okręgu.')
print('2 obwód okręgu')
wybor = int(input('wbierz opcję 1 lub 2: '))
if wybor == 1:
    pole_okregu = pi * (srednica_okregu / 2) ** 2
    print(f'Pole okręgu o średnicy {srednica_okregu} jest równe {pole_okregu}')
elif wybor == 2:
    obwod_okregu = pi * srednica_okregu
    print(f'Obwód okręgu o średnicy {srednica_okregu} jest równe {obwod_okregu}')
else:
    print('Nie ma takiej opcji')

#Zadanie 3
cena_konsoli = float(input('Podaj cene konsoli: '))
ilosc = int(input('Podaj ilosc: '))
rabat = float(input('Podaj rabat: '))

print('Co mam obliczyć:')
print('1 kwotę całego zamówienia.')
print('2 koszt jednej konsoli z uwzględnieniem rabatu')
wybor = int(input('wbierz opcję 1 lub 2: '))

if wybor == 1:
    kwota_zamówienia = cena_konsoli * ilosc * (1 - rabat)
    print(f'Kwota zamówienia jest równa {kwota_zamówienia}')
elif wybor == 2:
    koszt_konsoli_po_rabacie = cena_konsoli * (1 - rabat)
    print(f'Ceana konsoli z uwzględnieniem rabatu jest równa {koszt_konsoli_po_rabacie}')
else:
    print('Nie ma takiej opcji')

#Zadanie 4
rozmiar_pliku_w_GB = float(input('Podaj rozmiar pliku w GB: '))
przepustowosc_w_bt = float(input('Podaj przepustowosc w bitach / sec: '))
print('Oblicz czas pobierania pliku:')
print('1 w godzinach')
print('2 w minutach')
print('3 w sekundach')

czas_pobierania_w_sec = 8000000000 / przepustowosc_w_bt

if wybor == 1:
    czas_pobierania_w_godzinach = czas_pobierania_w_sec / 3600
    print(f'Czas pobierania pliku to {czas_pobierania_w_godzinach} godzin')
elif wybor == 2:
    czas_pobierania_w_min = czas_pobierania_w_sec / 60
    print(f'Czas pobierania pliku to {czas_pobierania_w_min} min')
elif wybor == 3:
    print(f'Czas pobierania pliku to {czas_pobierania_w_sec} sec')
else:
    print('Nie ma takiej opcji')

#Zadanie 5
godzina = int(input('Podaj godzinę od 0 do 23: '))
if godzina >= 0 and godzina < 6:
    print('Good Night')
elif godzina >= 6 and godzina < 13:
    print('Good Morning')
elif godzina >= 13 and godzina < 17:
    print('Good Day')
elif godzina >= 17 and godzina < 24:
    print('Good Evening')





