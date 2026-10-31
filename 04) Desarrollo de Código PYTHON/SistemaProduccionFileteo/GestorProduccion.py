class GestorProduccion:
    def __init__(self):
        self._registros = []

    def agregar_registro(self, registro):
        self._registros.append(registro)

    # Cerrar el registro y resumir los rendimientos
    def cerrar_registro_fileteo(self):
        buenos = 0
        malos = 0

        for registro in self._registros:
            evaluacion = registro.evaluar_rendimiento()

            if evaluacion == "Rendimiento Bueno":
                buenos += 1
            else:
                malos += 1

        print("=== CIERRE DE REGISTRO DE FILETEO ===")
        print(
            f"Total de registros evaluados: "
            f"{len(self._registros)}"
        )
        print(f"Productos con Rendimiento Bueno: {buenos}")
        print(f"Productos con Rendimiento Malo: {malos}")
        