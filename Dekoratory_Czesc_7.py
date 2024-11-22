import time

# Zadanie 1

class ZmierzCzasDziałania:
    def __init__(self, funkcja):
        self.funkcja = funkcja
        self._startTime = 0
        self._endTime = 0

    def __call__(self, *args, **kwargs):
        self._startTime = time.time()
        fun = self.funkcja(*args, **kwargs)
        self._endTime = time.time()
        print(self._endTime - self._startTime)
        return fun

@ZmierzCzasDziałania
def wyznacz_pierwsze(n):
    pierwsze = [2]

    def czy_pierwsza(liczba):
        for dzielnik in pierwsze:
            if liczba % dzielnik == 0:
                return False
            if dzielnik * dzielnik > liczba:
                return True
        return True

    for i in range(2, n):
        if czy_pierwsza(i):
            pierwsze.append(i)
    return pierwsze

print(wyznacz_pierwsze(10000))

#Zadanie 2

@ZmierzCzasDziałania
def wyznacz_pierwsze(start, end):
    pierwsze = [2]
    pierwsze_start_end = []

    def czy_pierwsza(liczba):
        for dzielnik in pierwsze:
            if liczba % dzielnik == 0:
                return False
            if dzielnik * dzielnik > liczba:
                return True
        return True

    for i in range(2, end):
        if czy_pierwsza(i):
            pierwsze.append(i)
            if start <= i and i <= end:
                pierwsze_start_end.append(i)
    return pierwsze_start_end

print(wyznacz_pierwsze(100,10000))

#Zadanie 3

class SprawozdanieFinansoweDekorator:

    def __init__(self, funkcja):
        self.funkcja = funkcja
        self._formaty_sprawozdan = {"agencja 1":"format sprawozdania dla agencji 1", "agencja 2":"format sprawozdania dla agencji 2"}

    def __call__(self,agencja, *args, **kwargs):
        print(self._formaty_sprawozdan[agencja])
        self.funkcja(agencja, *args, **kwargs)

@SprawozdanieFinansoweDekorator
def sprawozdanie(agencja):
    print("Dane finansowe firmy")

sprawozdanie("agencja 2")

sprawozdanie("agencja 1")