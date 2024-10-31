# Zadanie 1

class Samochod:

    def __init__(self, model, rok_wydania, producent, pojemnosc_silnika, kolor, cena):
        self.__model = model
        self.__rok_wydania = rok_wydania
        self.__producent = producent
        self.__pojemnosc_silnika = pojemnosc_silnika
        self.__kolor = kolor
        self.__cena = cena

    def set_model(self, model):
        self.__model = model

    def set_rok_wydania(self, rok_wydania):
        self.__rok_wydania = rok_wydania

    def set_producent(self, producent):
        self.__producent = producent

    def set_pojemnosc_silnika(self, pojemnosc_silnika):
        self.__pojemnosc_silnika = pojemnosc_silnika

    def set_kolor(self, kolor):
        self.__kolor = kolor

    def set_cena(self, cena):
        self.__cena = cena

    def get_model(self):
        return self.__model

    def get_rok_wydania(self):
        return self.__rok_wydania

    def get_producent(self):
        return self.__producent

    def get_pojemnosc_silnika(self):
        return self.__pojemnosc_silnika

    def get_kolor(self):
        return self.__kolor

    def get_cena(self):
        return self.__cena


s = Samochod('RAV 4', '2024-01-15', 'Toyota', 2.0, 'czarny', 180000)
print(s.get_model(), s.get_rok_wydania(), s.get_producent(), s.get_pojemnosc_silnika(), s.get_kolor(), s.get_cena())

# Zadanie 2

class Book:

    def __init__(self, tytul, rok_wydania, wydawca, gatunek, autor, cena):
        self.__tytul = tytul
        self.__rok_wydania = rok_wydania
        self.__wydawca = wydawca
        self.__gatunek = gatunek
        self.__autor = autor
        self.__cena = cena

    def set_tytul(self, tytul):
        self.__tytul = tytul

    def set_rok_wydania(self, rok_wydania):
        self.__rok_wydania = rok_wydania

    def set_wydawca(self, wydawca):
        self.__wydawca = wydawca

    def set_gatunek(self, gatunek):
        self.__gatunek = gatunek

    def set_autor(self, autor):
        self.__autor = autor

    def set_cena(self, cena):
        self.__cena = cena

    def get_tytul(self):
        return self.__tytul

    def get_rok_wydania(self):
        return self.__rok_wydania

    def get_wydawca(self):
        return self.__wydawca

    def get_gatunek(self):
        return self.__gatunek

    def get_autor(self):
        return self.__autor

    def get_cena(self):
        return self.__cena


b = Book('Rodzinny interes', '2024', 'Wydawnictwo Marginesy', 'Kryminał', 'Wojciech Chmielarz', 29.16)
print(b.get_tytul(), b.get_rok_wydania(),b.get_wydawca(), b.get_gatunek(), b.get_autor(), b.get_cena())

# Zadanie 3

class Stadium:

    def __init__(self, nazwa_stadionu, data_otwarcia, kraj, miasto, liczba_miejsc_siedzacych):
        self.__nazwa_stadionu = nazwa_stadionu
        self.__data_otwarcia = data_otwarcia
        self.__kraj = kraj
        self.__miasto = miasto
        self.__liczba_miejsc_siedzacych = liczba_miejsc_siedzacych

    def set_nazwa_stadionu(self, nazwa_stadionu):
        self.__nazwa_stadionu = nazwa_stadionu

    def set_data_otwarcia(self, data_otwarcia):
        self.__data_otwarcia = data_otwarcia

    def set_kraj(self, kraj):
        self.__kraj = kraj

    def set_miasto(self, miasto):
        self.__miasto = miasto

    def set_liczba_miejsc_siedzacych(self, liczba_miejsc_siedzacych):
        self.__liczba_miejsc_siedzacych = liczba_miejsc_siedzacych

    def get_nazwa_stadionu(self):
        return self.__nazwa_stadionu

    def get_data_otwarcia(self):
        return self.__data_otwarcia

    def get_kraj(self):
        return self.__kraj

    def get_miasto(self):
        return self.__miasto

    def get_liczba_miejsc_siedzacych(self):
        return self.__liczba_miejsc_siedzacych


st = Stadium('Stadion Cracovii im. Józefa Piłsudskiego','1912-03-31', 'Polska', 'Kraków', 15016)

print(st.get_nazwa_stadionu(), st.get_data_otwarcia(), st.get_kraj(), st.get_miasto(), st.get_liczba_miejsc_siedzacych())
