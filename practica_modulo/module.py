# module.py

# !/usr/bin/env python3

""" module.py - an example of Python module """

__counter = 0


def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum


def prodl(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod


def readint(prompt, min, max):
    try:
        read = int(input(prompt))
        assert min < read < max
        return read
    except ValueError:
        print("Error: entrada incorrecta")
        return readint(prompt, min, max)
    except AssertionError:
        print(f"Error: el valor no está dentro del rango permitido ({min}..{max})")
        return readint(prompt, min, max)


def searchOcurrencesText(txt, subtxt):
    fnd = txt.find(subtxt)
    while fnd != -1:
        print(fnd)
        fnd = txt.find(subtxt, fnd + 1)


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


def printExcTree(thisclass, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)

print(__name__)

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i + 1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)
    printExcTree(BaseException)
