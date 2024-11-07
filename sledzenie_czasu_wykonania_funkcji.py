import time
import random


def fun_wait():
    i = random.randint(1, 10)
    time.sleep(i)


def miernik_wykonania(f):
    licznik = 0

    def zmierz_czas():
        nonlocal licznik
        licznik += 1
        t = time.time()
        f()
        return [time.time() - t, licznik]

    return zmierz_czas


miernik = miernik_wykonania(fun_wait)

for i in range(5):
    m = miernik()
    print(f'Czas wykonania funkcji: {m[0]} ilość pomiarów: {m[1]}')

