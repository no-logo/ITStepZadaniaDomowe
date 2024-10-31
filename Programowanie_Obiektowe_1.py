# Zadanie 1

class Samochod:
    __model = ''
    __rok_wydania = ''
    __producent = ''
    __pojemnosc_silnika = 0
    __kolor = ''
    __cena = 0

    @classmethod
    def set_model(cls, model):
        cls.__model = model

    @classmethod
    def set_rok_wydania(cls, rok_wydania):
        cls.__rok_wydania = rok_wydania

    @classmethod
    def set_producent(cls, producent):
        cls.__producent = producent

    @classmethod
    def set_pojemnosc_silnika(cls, pojemnosc_silnika):
        cls.__pojemnosc_silnika = pojemnosc_silnika

    @classmethod
    def set_kolor(cls, kolor):
        cls.__kolor = kolor

    @classmethod
    def set_cena(cls, cena):
        cls.__cena = cena

    @classmethod
    def get_model(cls):
        return cls.__model

    @classmethod
    def get_rok_wydania(cls):
        return cls.__rok_wydania

    @classmethod
    def get_producent(cls):
        return cls.__producent

    @classmethod
    def get_pojemnosc_silnika(cls):
        return cls.__pojemnosc_silnika

    @classmethod
    def get_kolor(cls):
        return cls.__kolor

    @classmethod
    def get_cena(cls):
        return cls.__cena

Samochod.set_model ('RAV 4')
Samochod.set_rok_wydania('2024-01-15')
Samochod.set_producent('Toyota')
Samochod.set_pojemnosc_silnika(2.0)
Samochod.set_kolor('czarny')
Samochod.set_cena(180000)

print(Samochod.get_model(), Samochod.get_rok_wydania(), Samochod.get_producent(), Samochod.get_pojemnosc_silnika(), Samochod.get_kolor(), Samochod.get_cena())

# Zadanie 2

class Book:
    __tytul = ''
    __rok_wydania = ''
    __wydawca = ''
    __gatunek = ''
    __autor = ''
    __cena = ''

    @classmethod
    def set_tytul(cls, tytul):
        cls.__tytul = tytul

    @classmethod
    def set_rok_wydania(cls, rok_wydania):
        cls.__rok_wydania = rok_wydania

    @classmethod
    def set_wydawca(cls, wydawca):
        cls.__wydawca = wydawca

    @classmethod
    def set_gatunek(cls, gatunek):
        cls.__gatunek = gatunek

    @classmethod
    def set_autor(cls, autor):
        cls.__autor = autor

    @classmethod
    def set_cena(cls, cena):
        cls.__cena = cena

    @classmethod
    def get_tytul(cls):
        return cls.__tytul

    @classmethod
    def get_rok_wydania(cls):
        return cls.__rok_wydania

    @classmethod
    def get_wydawca(cls):
        return cls.__wydawca

    @classmethod
    def get_gatunek(cls):
        return cls.__gatunek

    @classmethod
    def get_autor(cls):
        return cls.__autor

    @classmethod
    def get_cena(cls):
        return cls.__cena

Book.set_tytul('Rodzinny interes')
Book.set_rok_wydania('2024')
Book.set_wydawca('Wydawnictwo Marginesy')
Book.set_gatunek('Kryminał')
Book.set_autor('Wojciech Chmielarz')
Book.set_cena(29.16)

print(Book.get_tytul(), Book.get_rok_wydania(),Book.get_wydawca(), Book.get_gatunek(), Book.get_autor(), Book.get_cena())

# Zadanie 3

class Stadium:
    __nazwa_stadionu = ''
    __data_otwarcia = ''
    __kraj = ''
    __miasto = ''
    __liczba_miejsc_siedzących = 0

    @classmethod
    def set_nazwa_stadionu(cls, nazwa_stadionu):
        cls.__nazwa_stadionu = nazwa_stadionu

    @classmethod
    def set_data_otwarcia(cls, data_otwarcia):
        cls.__data_otwarcia = data_otwarcia

    @classmethod
    def set_kraj(cls, kraj):
        cls.__kraj = kraj

    @classmethod
    def set_miasto(cls, miasto):
        cls.__miasto = miasto

    @classmethod
    def set_liczba_miejsc_siedzących(cls,liczba_miejsc_siedzących):
        cls.__liczba_miejsc_siedzących = liczba_miejsc_siedzących

    @classmethod
    def get_nazwa_stadionu(cls):
        return cls.__nazwa_stadionu

    @classmethod
    def get_data_otwarcia(cls):
        return cls.__data_otwarcia

    @classmethod
    def get_kraj(cls):
        return cls.__kraj

    @classmethod
    def get_miasto(cls):
        return cls.__miasto

    @classmethod
    def get_liczba_miejsc_siedzących(cls):
        return cls.__liczba_miejsc_siedzących

Stadium.set_nazwa_stadionu('Stadion Cracovii im. Józefa Piłsudskiego')
Stadium.set_data_otwarcia('1912-03-31')
Stadium.set_kraj('Polska')
Stadium.set_miasto('Kraków')
Stadium.set_liczba_miejsc_siedzących(15016)

print(Stadium.get_nazwa_stadionu(), Stadium.get_data_otwarcia(), Stadium.get_kraj(), Stadium.get_miasto(), Stadium.get_liczba_miejsc_siedzących())
