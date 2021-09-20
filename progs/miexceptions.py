class ExcepcionDatosAlumnos(Exception):
    pass


class LineaErronea(ExcepcionDatosAlumnos):
    def __init__(self, mensaje='Linea del archivo erronea'):
        super().__init__(self, mensaje)


class ArchivoVacio(ExcepcionDatosAlumnos):
    def __init__(self, mensaje='Archivo de notas vacio'):
        super().__init__(self, mensaje)
