#Zadanie 1

class WrongAgeException(Exception):
    pass

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 0 or age > 130:
        raise WrongAgeException("age out of range")
    print(f"Hello, {name}! Your age is {age}")
except WrongAgeException as e:
    print(e)
except ValueError as e:
    print(e)
