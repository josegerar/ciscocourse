from random import randint, randrange


class TicTacToe(object):
    board: list[list[str]] = None
    digit_machine: str = 'X'
    digit_user: str = 'O'
    movimientos: int = 0
    ganador = False

    def __init__(self):
        self.board = [[str(x + 1) for x in range(y * 3, y * 3 + 3)] for y in range(3)]

        while not self.ganador:
            self.DrawMove()

            self.DisplayBoard()

            self.ganador = self.VictoryFor(self.digit_machine)
            if self.ganador:
                print("Te han ganado")
                continue
            elif self.movimientos == 9:
                self.ganador = True
                print("Han empatado")
                continue

            self.EnterMove()

            self.DisplayBoard()

            self.ganador = self.VictoryFor(self.digit_user)
            if self.ganador:
                print("Has ganado")
                continue
            elif self.movimientos == 9:
                self.ganador = True
                print("Han empatado")

    def DisplayBoard(self):
        # la función acepta un parámetro el cual contiene el estado actual del tablero
        # y lo muestra en la consola
        for i in range(3):
            print("+-------+-------+-------+")
            print("|       |       |       |")
            valores = ""
            for j in range(3):
                valores += "|   " + self.board[i][j] + "   "
            valores += "|"
            print(valores)
            print("|       |       |       |")
            print("+-------+-------+-------+")

    def EnterMove(self):
        # la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
        # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
        mov_user = int(input("Ingresa tu movimiento: "))
        valido = False

        while not valido:
            if mov_user < 1 or mov_user > 9:
                print("Ingresa un numero valido entre 1 y 9")
                mov_user = int(input("Ingresa tu movimiento: "))
                continue

            movimientos_validos = self.MakeListOfFreeFields()
            for i, j in movimientos_validos:
                if int(self.board[i][j]) == mov_user:
                    self.board[i][j] = self.digit_user
                    valido = True
                    break

        self.movimientos += 1

    def MakeListOfFreeFields(self):
        # la función examina el tablero y construye una lista de todos los cuadros vacíos
        # la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
        lista = list()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] not in [self.digit_machine, self.digit_user]:
                    lista.append((i, j,))

        return lista

    def VictoryFor(self, sing):
        # la función analiza el estatus del tablero para verificar si
        # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
        if (self.board[0][0] == sing and self.board[1][1] == sing and self.board[2][2] == sing) \
                or (self.board[2][0] == sing and self.board[1][1] == sing and self.board[0][2] == sing):
            return True

        for i in range(3):
            if (self.board[i][0] == sing and self.board[i][1] == sing and self.board[i][2] == sing) \
                    or (self.board[0][i] == sing and self.board[1][i] == sing and self.board[2][i] == sing):
                return True
        return False

    def DrawMove(self):
        # la función dibuja el movimiento de la maquina y actualiza el tablero

        if self.movimientos == 0:
            self.board[1][1] = self.digit_machine
            self.movimientos += 1
            return

        movimientos_validos = self.MakeListOfFreeFields()

        aleatorio = randrange(len(movimientos_validos))

        movimiento_seleccionado = movimientos_validos[aleatorio]

        self.board[movimiento_seleccionado[0]][movimiento_seleccionado[1]] = self.digit_machine

        self.movimientos += 1
