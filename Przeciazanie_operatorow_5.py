
#Zadanie 1

class Circle:
    def __init__(self, r):
        self.__radius = r

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            if self.__radius < other.__radius:
                return True
            else:
                return False
        else:
            return NotImplemented


    def __le__(self, other):
        if isinstance(other, Circle):
            if self.__radius <= other.__radius:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            if self.__radius > other.__radius:
                return True
            else:
                return False
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            if self.__radius >= other.__radius:
                return True
            else:
                return False
        else:
            return NotImplemented


c1 = Circle(10)
c2 = Circle(10)
c3 = Circle(5)

print(c1==c2)
print(c1==c3)
print(c1>=c2)
print(c1>c2)
print(c1<c3)
print(c1<=c3)

#Zadanie 2

class Complex:
    def __init__(self, real, imag):
        self.__r = real
        self.__i = imag

    def __str__(self):
        return f'cx = {self.__r} + {self.__i}i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__r + other.__r, self.__i + other.__i)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__r - other.__r, self.__i - other.__i)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__r * other.__r, self.__i * other.__i)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__r / other.__r, self.__i * other.__i)
        return NotImplemented

cx1 = Complex(6, 4)
cx2 = Complex(3, 2)

print(cx1 + cx2)
print(cx1 - cx2)
print(cx1 * cx2)
print(cx1 / cx2)

#Zadanie 3

class Plane:
    def __init__(self, nop):
        self.__number_of_passengers = nop

    def __add__(self, other):
        if isinstance(other, Plane):
            return Plane(self.__number_of_passengers + other.__number_of_passengers)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Plane):
            return Plane(self.__number_of_passengers - other.__number_of_passengers)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Plane):
            self.__number_of_passengers += other.__number_of_passengers
            return self
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Plane):
            self.__number_of_passengers -= other.__number_of_passengers
            return self
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Plane):
            return Plane(self.__number_of_passengers > other.__number_of_passengers)
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Plane):
            return Plane(self.__number_of_passengers >= other.__number_of_passengers)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Plane):
            return Plane(self.__number_of_passengers < other.__number_of_passengers)
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Plane):
            return Plane(self.__number_of_passengers <= other.__number_of_passengers)
        else:
            return NotImplemented

#Zadanie 4

class Apartment:
    def __init__(self, area, price):
        self.__area = area
        self.__price = price

    def __eq__(self, other):
        if isinstance(other, Apartment):
            return self.__area == other.__area
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Apartment):
            return self.__area != other.__area
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Apartment):
            return self.__price > other.__price
        else:
            return NotImplemented



