    public class OperarioProduccion {
    private String codigo;
    private String nombre;
    private String turno;

    public OperarioProduccion(String codigo, String nombre, String turno) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.turno = turno;
    }

    public String getCodigo() { return codigo; }
    public String getNombre() { return nombre; }
    public String getTurno() { return turno; }
}
