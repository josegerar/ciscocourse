# main.py

from sys import path

path.append('..\\modules')
print(__name__)

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))