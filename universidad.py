from persona import Persona

class Universidad:
    def __init__(self, nombre, codigoUniversidad,tipo):
        self.nombre = nombre
        self.codigoUniversidad = codigoUniversidad
        self.tipo = tipo
        self.personas = []
        self.personas1 = []

    def agregar_persona(self,persona :Persona,tip_persona):
        if tip_persona == 0:  #profesores
          self.personas.append(persona)
        else: #estudiantes
          self.personas1.append(persona)  

    def listar_personas(self):
        print(f"-----Listado en la univeridad {self.nombre} -----") 
        for p in self.personas:
            p.mostrar_info()

        for x in self.personas1:
            x.mostrar_info()

    #tarea
    def buscar_personas(self, nombre):
        for p in self.personas:
           if p.nombre == nombre:
                print(f"'{nombre}' se encuentra en Lista")

    def listar_estudiantes(self):
        print(f"-----Listado de ESTUDIANTES -----") 
        for p in self.personas1:
            p.mostrar_info()  

    def listar_profesores(self):
        print(f"-----Listado de PROFESORES -----") 
        for p in self.personas:
            p.mostrar_info()  


    # Contar cuántos estudiantes hay en cada carrera(cabreracastillon_001)
    
    def contar_estudiantes_por_carrera(self):
        conteo = {}
        for est in self.personas1:   # recorres la lista de estudiantes
            if est.carrera in conteo:
                conteo[est.carrera] += 1
            else:
                conteo[est.carrera] = 1
        
        print("---- Estudiantes por carrera ----")
        for carrera, cantidad in conteo.items():
            print(f"{carrera}: {cantidad}")

    # Listar profesores por especialidad (cabreracastillon_001)
    
    def listar_profesores_por_especialidad(self, especialidad):
        print(f"---- Profesores de {especialidad} ----")
        for prof in self.personas:
            if prof.especialidad == especialidad:
                prof.mostrar_info()
