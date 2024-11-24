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

#Zadanie 2A

class WrongAgeException(Exception):
    pass

def format_hello_message(name, age):
    return f"Hello, {name}! Your age is {age}"

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 0 or age > 130:
        raise WrongAgeException("age out of range")
    print(format_hello_message(name, age))
except WrongAgeException as e:
    print(e)
except ValueError as e:
    print(e)


