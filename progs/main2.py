from itertools import groupby
from os import strerror
import string

from progs.miexceptions import LineaErronea, ArchivoVacio


def read():
    try:
        ccnt = lcnt = 0
        for line in open('text.txt', 'rt', encoding="utf-8"):
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        print("\n\nCaracteres en el archivo: ", ccnt)
        print("Lineas en el archivo:     ", lcnt)
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


def write():
    try:
        fo = open('newtext.txt', 'wt')  # un nuevo archivo (newtext.txt) es creado
        for i in range(10):
            s = "línea #" + str(i + 1) + "\n"
            for ch in s:
                fo.write(ch)
        fo.close()
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


def writebyte():
    data = bytearray(10)

    for i in range(len(data)):
        data[i] = 10 + i

    try:
        bf = open('file.bin', 'wb')
        bf.write(data)
        bf.close()
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


def readbyte():
    from os import strerror

    data = bytearray(10)

    try:
        bf = open('file.bin', 'rb')
        bf.readinto(data)
        bf.close()

        for b in data:
            print(hex(b), end=' ')
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


def laboratorio1(srcname):
    letras_encontradas = {}
    letras_validas = string.ascii_lowercase
    try:
        src = open(srcname, 'rt', encoding="utf-8")
    except IOError as e:
        print("No se puede abrir archivo fuente: ", strerror(e.errno))
        exit(e.errno)

    for line in src:
        print(line, end="")
        for ch in line:
            ch = ch.lower()
            if ch in letras_validas:
                if ch in letras_encontradas:
                    letras_encontradas[ch] += 1
                else:
                    letras_encontradas[ch] = 1

    src.close()

    for key in letras_encontradas.keys():
        print(f"{key} -> {letras_encontradas[key]}")

    return letras_encontradas


def laboratorio2():
    srcname = input("¿Nombre del archivo fuente?: ")
    letras_encontradas = laboratorio1(srcname)
    letras_list = [(x, letras_encontradas[x]) for x in letras_encontradas.keys()]
    letras_list.sort(key=lambda x: x[1], reverse=True)
    try:
        fo = open(srcname + ".hist", 'wt')  # un nuevo archivo (newtext.txt) es creado
        for i in letras_list:
            s = f"{i[0]} -> {str(i[1])}\n"
            for ch in s:
                fo.write(ch)
        fo.close()
    except IOError as e:
        print("Se produjo un error de E/S: ", strerror(e.errno))


def laboratorio3():
    srcname = input("¿Nombre del archivo fuente?: ")
    try:
        src = open(srcname, 'rt', encoding="utf-8")
    except IOError as e:
        print("No se puede abrir archivo fuente: ", strerror(e.errno))
        exit(e.errno)

    lista_notas = []
    try:
        for line in src:
            line = line.replace("\n", "")
            line_split = line.split("\t")

            if len(line_split) != 3:
                raise LineaErronea

            lista_notas.append(line_split)

        if len(lista_notas) == 0:
            raise ArchivoVacio

    except LineaErronea as e:
        print(e.__str__())
    except ArchivoVacio as a:
        print(a.__str__())

    informe = []
    for i in lista_notas:
        existe = False
        for j, k in enumerate(informe):
            if i[0] == k[0] and i[1] == k[1]:
                existe = True
                break
        if existe:
            informe[j][2] = float(informe[j][2]) + float(i[2])
        else:
            informe.append(i)

    informe.sort(key=lambda x: x[0])
    for item in informe:
        message = f"{item[0]} {item[1]}"
        message += " " * (20 - (len(message) % 20) + 1)
        message += str(item[2])
        print(message)


laboratorio3()
