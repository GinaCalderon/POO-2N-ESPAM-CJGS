class OperarioProduccion:
    def __init__(self, codigo, nombre, turno):
        self._codigo = codigo
        self._nombre = nombre
        self._turno = turno

    # Getters para consultar los atributos
    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_turno(self):
        return self._turno
    