import math
import sys
from random import randrange
from typing import Union

from python_basico.tictactoe import TicTacToe


def ordenamiento_burbuja():
    miLista = [8, 10, 6, 2, 4]  # lista para ordenar
    swapped = True  # lo necesitamos verdadero (True) para ingresar al bucle while

    while swapped:
        swapped = False  # no hay swaps hasta ahora
        for i in range(len(miLista) - 1):
            if miLista[i] > miLista[i + 1]:
                swapped = True  # ocurrió el intercambio!
                miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

    print(miLista)


def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysInMonth(year, month):
    if month < 1 or month > 12 or year < 1582:
        return None

    dias_de_cada_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    es_biciesto = isYearLeap(year)

    if es_biciesto and month == 2:
        return dias_de_cada_mes[month - 1] + 1

    return dias_de_cada_mes[month - 1]


def dayOfYear(year, month, day):
    days_in_month = daysInMonth(year, month)
    if days_in_month is None or days_in_month < day or day < 1:
        return None

    dias_totales = 0

    if month == 1:
        return daysInMonth(year, month)

    for i in range(month - 1):
        dias_totales += daysInMonth(year, i + 1)

    return dias_totales + day


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def l100kmtompg(liters):
    metros_en_milla = 1_609.344
    litros_en_galon = 3.785411784
    return (1000 / metros_en_milla) / ((1 / litros_en_galon) * (liters / 100))


def mpgtol100km(miles):
    metros_en_milla = 1_609.344
    litros_en_galon = 3.785411784
    kilometros_recorridos = miles * (metros_en_milla / 1000)
    proporcion_litros = litros_en_galon / kilometros_recorridos
    return proporcion_litros * 100


def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or peso < 20 or peso > 200:
        return None

    return peso / altura ** 2


def lbakg(lb):
    return lb * 0.45359237


def piepulgam(pie, pulgada=0.0):
    return pie * 0.3048 + pulgada * 0.0254


def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b


def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto


def factorialFun_recusivo(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)


def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum


def fib_recursivo(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def saluda():
    papa = 2
    print("Hola", papa)


def fun(a, b):
    return b ** a


def misplit(strng):
    mi_list = []
    strng = strng.strip()
    fnd = strng.find(" ")
    index = 0
    if len(strng) > 0 and strng.count(" ") == 0:
        mi_list.append(strng)

    if len(strng) > 0 and strng.count(" ") > 0:
        mi_list.append(strng[index:fnd])
        index = fnd + 1

    while fnd != -1:
        fnd = strng.find(" ", fnd + 1)
        if fnd == -1:
            mi_list.append(strng[index:])
            continue
        mi_list.append(strng[index:fnd])
        index = fnd + 1

    return mi_list


def display_led(_value):
    _value = str(_value)

    if int(_value) < 0:
        raise ValueError("Debe ingresar un nuemro mayor a 0")

    representations = {
        '0': ('###', '# #', '# #', '# #', '###'),
        '1': ('  #', '  #', '  #', '  #', '  #'),
        '2': ('###', '  #', '###', '#  ', '###'),
        '3': ('###', '  #', '###', '  #', '###'),
        '4': ('# #', '# #', '###', '  #', '  #'),
        '5': ('###', '#  ', '###', '  #', '###'),
        '6': ('###', '#  ', '###', '# #', '###'),
        '7': ('###', '  #', '  #', '  #', '  #'),
        '8': ('###', '# #', '###', '# #', '###'),
        '9': ('###', '# #', '###', '  #', '###'),
        '.': ('   ', '   ', '   ', '   ', '  #'),
    }
    # treat the number as a string, since that makes it easier to deal with
    # on a digit-by-digit basis
    digits = [representations[digit] for digit in _value]
    # now digits is a list of 5-tuples, each representing a digit in the given number
    # We'll print the first lines of each digit, the second lines of each digit, etc.
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))


def cifrado_cesar(_str: str):
    cifrado = ''
    for char in _str:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cifrado += chr(code)
    return cifrado


def descifrado_cesar(_str: str):
    text = ''
    for char in _str:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)

    return text


def validador_iban(iban: str):
    iban = iban.replace(' ', '')
    if not iban.isalnum():
        print("Has introducido caracteres no válidos.")
    elif len(iban) < 15:
        print("El IBAN ingresado es demasiado corto.")
    elif len(iban) > 31:
        print("El IBAN ingresado es demasiado largo.")
    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)
        if ibann % 97 == 1:
            print("El IBAN ingresado es válido.")
        else:
            print("El IBAN ingresado no es válido.")


def es_palindromo(_str: str):
    _str = _str.lower()
    _str = "".join(_str.split())
    reverse_str = list(_str)
    reverse_str.reverse()
    _reversed = "".join(reverse_str)
    if _reversed == _str:
        print("Es palidromo")
    else:
        print("No es palindromo")


def es_anagrama(_str1: str, _str2: str):
    _es = "Anagramas"
    _no_es = "No son Anagramas"
    _str2 = _str2.lower()
    _str1 = _str1.lower()
    if len(_str2) != len(_str1):
        return _no_es
    for _char in _str1:
        if _str1.count(_char) != _str2.count(_char):
            return _no_es
    return _es


def digit_life(_str: str):
    if not _str.isnumeric():
        raise ValueError("Debe ingresar solo valores numericos")

    if len(_str) < 6 or len(_str) > 8:
        raise ValueError("Ingrese un formato correcto")
    _digit = 0
    for _char in _str:
        _digit += int(_char)

    while len(str(_digit)) > 1:
        _str = str(_digit)
        _digit = 0
        for _char in _str:
            _digit += int(_char)

    return _digit


def hide_characters(_str_search: str, _str_searching: str):
    index = 0
    for _char in _str_search:
        fnd = _str_searching.find(_char, index)
        if fnd == -1:
            return "No"
        index = fnd + 1

    return "Si"


def es_sudoku_valido(_array: list):
    for _fila in _array:
        _fila_set = set(_fila)
        if len(_fila_set) != len(_fila):
            return "No"

    for _index in range(len(_array)):
        _col = [_array[_col_index][_index] for _col_index in range(len(_array[_index]))]
        _col_set = set(_col)
        if len(_col_set) != len(_col):
            return "No"

    for h in range(3):
        for i in range(0, len(_array), 3):
            _sub_cuadro = []

            for j in range(0, 3):
                _sub_cuadro += _array[i + j][h * 3:(h * 3) + 3]

            _sub_cuadro_set = set(_sub_cuadro)
            if len(_sub_cuadro_set) != len(_sub_cuadro):
                return "No"

    return "Si"


if __name__ == '__main__':
    validador_iban("GB72 HBZU 7006 7212 1253 00")
    validador_iban("FR76 30003 03620 00020216907 50")
    validador_iban("DE02100100100152517108")
    print("12344".find("2"))
    print(chr(1))
    es_palindromo("Ten animals I slam in a net")
    print(es_anagrama("Listen", "Silent"))
    print(digit_life("20000101"))
    print(hide_characters("donut", "Nabucodonosor"))
    sudoku = [
        [2, 9, 5, 7, 4, 3, 8, 6, 1],
        [4, 3, 1, 8, 6, 5, 9, 2, 7],
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 6],
        [6, 1, 2, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 1, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [1, 5, 4, 9, 3, 8, 6, 7, 2],
    ]
    sudoku2 = [
        [1, 9, 5, 7, 4, 3, 8, 6, 2],
        [4, 3, 1, 8, 6, 5, 9, 2, 7],
        [8, 7, 6, 1, 9, 2, 5, 4, 3],
        [3, 8, 7, 4, 5, 9, 2, 1, 6],
        [6, 1, 2, 3, 8, 7, 4, 9, 5],
        [5, 4, 9, 2, 1, 6, 7, 3, 8],
        [7, 6, 3, 5, 2, 4, 1, 8, 9],
        [9, 2, 8, 6, 7, 1, 3, 5, 4],
        [2, 5, 4, 9, 3, 8, 6, 7, 1],
    ]

    print(es_sudoku_valido(sudoku))
    print(es_sudoku_valido(sudoku2))

    fo = open("progs/text.txt", "r+")
    print("Name of the file: ", fo.name)

    line = fo.readlines()
    print("Read Line: %s" % (line))

    line = fo.readlines(2)
    print("Read Line: %s" % (line))

    # Close opened file
    fo.close()