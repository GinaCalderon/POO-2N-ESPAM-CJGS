import java.util.List;
import java.util.ArrayList;
class GestorProduccion {
    private List<RegistroFileteo> registros;

    public GestorProduccion() {
        this.registros = new ArrayList<>();
    }

    public void agregarRegistro(RegistroFileteo registro) {
        this.registros.add(registro);
    }

    // Método cerrarRegistroFileteo() reportando cuántos productos tuvieron rendimiento bueno y cuántos malo
    public void cerrarRegistroFileteo() {
        int buenos = 0;
        int malos = 0;

        for (RegistroFileteo reg : registros) {
            String evaluacion = reg.evaluarRendimiento();
            if (evaluacion.equals("Rendimiento Bueno")) {
                buenos++;
            } else {
                malos++;
            }
        }

        System.out.println("=== CIERRE DE REGISTRO DE FILETEO ===");
        System.out.println("Total de registros evaluados: " + registros.size());
        System.out.println("Productos con Rendimiento Bueno: " + buenos);
        System.out.println("Productos con Rendimiento Malo: " + malos);
    }
}
