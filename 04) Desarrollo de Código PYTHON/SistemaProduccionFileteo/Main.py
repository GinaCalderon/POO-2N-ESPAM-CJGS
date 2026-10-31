from datetime import datetime

from OperarioProduccion import OperarioProduccion
from RegistroFileteo import RegistroFileteo
from GestorProduccion import GestorProduccion


def main():
    op = OperarioProduccion(
        "OP-001",
        "Carlos Pérez",
        "Matutino"
    )

    gestor = GestorProduccion()

    try:
        # Ejemplo 1: masa correcta y rendimiento bueno
        reg1 = RegistroFileteo(
            "LOTE-100",
            100.0,
            48.0,
            52.0,
            op,
            fecha_produccion=datetime.now()
        )

        gestor.agregar_registro(reg1)

        print(
            "Registro 1 agregado correctamente. "
            f"Rendimiento: "
            f"{reg1.calcular_rendimiento_porcentaje()}% "
            f"-> {reg1.evaluar_rendimiento()}"
        )

        # Ejemplo 2: incumple la conservación de masa
        try:
            RegistroFileteo(
                "LOTE-101",
                100.0,
                40.0,
                50.0,
                op,
                fecha_produccion=datetime.now()
            )
        except ValueError as error:
            print(
                "Error detectado correctamente: "
                f"{error}"
            )

        # Ejemplo 3: masa correcta y rendimiento malo
        reg2 = RegistroFileteo(
            "LOTE-102",
            100.0,
            40.0,
            60.0,
            op
        )

        gestor.agregar_registro(reg2)

        print(
            "Registro 2 agregado correctamente. "
            f"Rendimiento: "
            f"{reg2.calcular_rendimiento_porcentaje()}% "
            f"-> {reg2.evaluar_rendimiento()}"
        )

        print()

        # Ejecutar el cierre de turno
        gestor.cerrar_registro_fileteo()

    except ValueError as error:
        print(f"Validación fallida: {error}")


if __name__ == "__main__":
    main()
