from persona import Persona

class Estudiante(Persona):

    def __init__(self,nombre,dni,edad,carrera):
        super().__init__(nombre,edad,dni)
        self.carrera = carrera
        self.__notas = []

    def agregar_nota(self,nota):
        if 0 <= nota <= 20:
            self.__notas.append(nota)
            print(f" Nota {nota} agregada correctamente")
            
        else:
            print(" Error: La nota debe estar entre 0 y 20")
            

    def promedio(self):
        promedio = 0
        cantidadnotas = len(self.__notas)
        suma = 0
        if(cantidadnotas == 0):
            return 0
        
        for nota in self.__notas:
            suma = suma + nota

        promedio = suma/cantidadnotas 

        return promedio
        '''
        return sum(self._notas) / len(self._notas) if self._notas else 0
        '''


    def mostrar_info(self):
        prom = self.promedio()
        print(f"Estudiante : {self.nombre}, Edad : {self.edad} Carrera: {self.carrera} , Con Promedio: {prom}")  

        # Nueva clase para gestionar estudiantes y poderlos eliminar

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