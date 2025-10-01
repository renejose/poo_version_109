from estudiante import Estudiante


class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"✅ Estudiante {estudiante.nombre} agregado correctamente.")

    def eliminar_estudiante(self, dni):
        for estudiante in self.estudiantes:
            if estudiante.dni == dni:
                self.estudiantes.remove(estudiante)
                print(f"🗑️ Estudiante con DNI {dni} eliminado correctamente.")
                return
        print(f"❌ No se encontró ningún estudiante con DNI {dni}.")

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("⚠️ No hay estudiantes registrados.")
            return
        for est in self.estudiantes:
            est.mostrar_info() 