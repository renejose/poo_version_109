from persona import Persona

class Profesor(Persona):
    def __init__(self,nombre,dni, edad,especialidad):
        super().__init__(nombre,edad,dni)
        self.especialidad = especialidad

    def mostrar_info(self):
        print(f"Profesor : {self.nombre}, Edad : {self.edad} Especialidad: {self.especialidad}")   