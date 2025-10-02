from persona import Persona

class Universidad:
    def __init__(self, nombre, codigoUniversidad,tipo):
        self.nombre = nombre
        self.codigoUniversidad = codigoUniversidad
        self.tipo = tipo
        self.personas = []

    def agregar_persona(self,persona :Persona):
        self.personas.append(persona)


    def listar_personas(self):
        print(f"-----Listado en la univeridad {self.nombre} -----") 
        for p in self.personas:
            p.mostrar_info()       