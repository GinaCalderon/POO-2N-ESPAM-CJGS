import java.util.Date;
// Flujo de ejecución 
public class Main {
    public static void main(String[] args) {
        OperarioProduccion op = new OperarioProduccion("OP-001", "Carlos Pérez", "Matutino");
        GestorProduccion gestor = new GestorProduccion();

        try {
            // Ejemplo 1: Cumple con la masa y da un rendimiento de 48% (Bueno)
            RegistroFileteo reg1 = new RegistroFileteo(new Date(), "LOTE-100", 100.0, 48.0, 52.0, op);
            gestor.agregarRegistro(reg1);
            System.out.println("Registro 1 agregado correctamente. Rendimiento: " + reg1.calcularRendimientoPorcentaje() + "% -> " + reg1.evaluarRendimiento());

            // Ejemplo 2: Rompe la regla de conservación de masa
            try {
                new RegistroFileteo (new Date (), "LOTE-101", 100.0, 40.0, 50.0, op);
            } catch (IllegalArgumentException e) {
                System.out.println("Error detectado correctamente: " + e.getMessage());
            }

            // Ejemplo 3: Cumple con la masa pero da un rendimiento de 40% (Malo)
            RegistroFileteo reg2 = new RegistroFileteo("LOTE-102", 100.0, 40.0, 60.0, op);
            gestor.agregarRegistro(reg2);
            System.out.println("Registro 2 agregado correctamente. Rendimiento: " + reg2.calcularRendimientoPorcentaje() + "% -> " + reg2.evaluarRendimiento());

            System.out.println();
            // Ejecutar el cierre de turno
            gestor.cerrarRegistroFileteo();

        } catch (IllegalArgumentException e) {
            System.err.println("Validación fallida: " + e.getMessage());
        }
    }
}
