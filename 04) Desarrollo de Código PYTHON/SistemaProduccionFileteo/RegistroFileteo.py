from datetime import datetime
class RegistroFileteo:
    def __init__(
        self,
        lote,
        peso_inicial,
        peso_lomos,
        peso_desperdicio,
        operario,
        fecha_produccion=None
    ):
        # Asignar fecha automáticamente si no se proporciona
        if fecha_produccion is None:
            fecha_produccion = datetime.now()

        # Validación 1: conservación de masa
        if abs(
            (peso_lomos + peso_desperdicio) - peso_inicial
        ) > 0.001:
            raise ValueError(
                "Error de Invariante de Masa: "
                "pesoLomos + pesoDesperdicio debe ser "
                "igual al pesoInicial."
            )

        # Validación 2: pesos válidos
        if (
            peso_inicial <= 0
            or peso_lomos < 0
            or peso_desperdicio < 0
        ):
            raise ValueError(
                "Los pesos no pueden ser negativos y "
                "el peso inicial debe ser mayor a cero."
            )

        # Atributos del registro
        self._fecha_produccion = fecha_produccion
        self._lote = lote
        self._peso_inicial = peso_inicial
        self._peso_lomos = peso_lomos
        self._peso_desperdicio = peso_desperdicio
        self._operario = operario

    # Calcular el porcentaje de rendimiento
    def calcular_rendimiento_porcentaje(self):
        return (self._peso_lomos / self._peso_inicial) * 100.0

    # Evaluar el rendimiento
    def evaluar_rendimiento(self):
        rendimiento = self.calcular_rendimiento_porcentaje()

        if 45.0 <= rendimiento <= 51.0:
            return "Rendimiento Bueno"
        else:
            return "Rendimiento Malo"

    # Getters
    def get_fecha_produccion(self):
        return self._fecha_produccion

    def get_lote(self):
        return self._lote

    def get_operario(self):
        return self._operario

    def get_peso_lomos(self):
        return self._peso_lomos

    def get_peso_desperdicio(self):
        return self._peso_desperdicio

    def get_peso_inicial(self):
        return self._peso_inicial