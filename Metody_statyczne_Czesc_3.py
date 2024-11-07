# Zadanie 1
print('\nZadanie 1\n')

from fractions import Fraction

class Fraction(Fraction):
    __fraction_counter = 0
    def __init__(self,numerator=0, denominator=None):
        super().__new__(Fraction, numerator, denominator)
        Fraction.__fraction_counter += 1

    @staticmethod
    def get_fraction_counter():
        return Fraction.__fraction_counter

f1 = Fraction(1,2)
f2 = Fraction(1,3)
f3 = Fraction(1,4)
print(f1, f2, f3)
print(f'Utworzono {Fraction.get_fraction_counter()} obiekty klasy {type(f1)}')

#Zadanie 2
print('\nZadanie 2\n')

class TemperatureConverter:
    __converter_counter = 0

    @staticmethod
    def convert_from_celsius_to_fahrenheit(temperature):
        TemperatureConverter.__converter_counter += 1
        f = 1.8 * temperature + 32
        return round(f,2)

    @staticmethod
    def convert_from_fahrenheit_to_celsius(temperature):
        TemperatureConverter.__converter_counter += 1
        c = (temperature - 32) / 1.8
        return round(c,2)

    @staticmethod
    def get_converter_counter():
        return TemperatureConverter.__converter_counter

print(TemperatureConverter.get_converter_counter())
print(TemperatureConverter.convert_from_celsius_to_fahrenheit(25))
print(TemperatureConverter.convert_from_fahrenheit_to_celsius(25))
print(TemperatureConverter.get_converter_counter())