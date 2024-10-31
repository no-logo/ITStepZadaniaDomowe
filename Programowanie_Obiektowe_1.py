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