from lief import not_implemented


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