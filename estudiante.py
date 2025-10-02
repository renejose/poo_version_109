from persona import Persona

class Estudiante(Persona):

    def __init__(self,nombre,dni,edad,carrera):
        super().__init__(nombre,edad,dni)
        self.carrera = carrera
        self.__notas = []
        self.estudiantesList = [] #tarea


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
        if prom >10:
           print(f"Alumno : {self.nombre} esta APROBADO") 
        else:
           print(f"Alumno : {self.nombre} esta DESAPROBADO")
    
        print(f"Clase Estud...Estudiante : {self.nombre}, Edad : {self.edad} Carrera: {self.carrera} , Con Promedio: {prom}") 

    #tarea
    def mostrar_si_aprobo():
        pass
    
    def agregarEst(self):
     self.estudiantesList.append(self.nombre)

    def listar_estudiante(self):
        for p in self.estudiantesList:
           print(f"{p}")

