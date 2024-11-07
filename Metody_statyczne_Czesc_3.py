# Zadanie 1
print('\nZadanie 1\n')

from fractions import Fraction

class FractionWithCounter(Fraction):
    __fraction_counter = 0
    def __init__(self,numerator=0, denominator=None):
        super().__new__(FractionWithCounter, numerator, denominator)
        FractionWithCounter.__fraction_counter += 1

    @staticmethod
    def get_fraction_counter():
        return FractionWithCounter.__fraction_counter

f1 = FractionWithCounter(1, 2)
f2 = FractionWithCounter(1, 3)
f3 = FractionWithCounter(1, 4)
print(f1, f2, f3)
print(f'Utworzono {FractionWithCounter.get_fraction_counter()} obiekty klasy {type(f1)}')

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

#Zadanie 3
print('\nZadanie 3\n')

class UnitsConverter:

    @staticmethod
    def convert_inch_to_cm(value):
        return value * 2.54

    @staticmethod
    def convert_cm_to_inch(value):
        return value / 2.54

    @staticmethod
    def convert_foot_to_cm(value):
        return value * 30.48

    @staticmethod
    def convert_cm_to_foot(value):
        return value / 30.48

    @staticmethod
    def convert_yard_to_m(value):
        return value * 0.9144

    @staticmethod
    def convert_m_to_yard(value):
        return value / 0.9144

    @staticmethod
    def convert_mile_to_km(value):
        return value * 1.6093

    @staticmethod
    def convert_km_to_mile(value):
        return value / 1.6093

    @staticmethod
    def convert_pint_to_ml(value):
        return value * 568

    @staticmethod
    def convert_ml_to_pint(value):
        return value / 568

    @staticmethod
    def convert_pound_to_g(value):
        return value * 453.59

    @staticmethod
    def convert_g_to_pound(value):
        return value / 453.59