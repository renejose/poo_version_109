from persona import Persona
from estudiante import Estudiante
from profesor import Profesor

class Universidad:
    def __init__(self, nombre, ruc, tipo):
        self.nombre = nombre
        self.ruc = ruc
        self.tipo = tipo
        self.personas = []   # lista de profesores y estudiantes

    def agregar_persona(self, persona: Persona):
        if isinstance(persona, Persona):
            self.personas.append(persona)
            print(f"Persona {persona.nombre} agregada a la universidad.")
        else:
            print("Solo se pueden agregar objetos de tipo Persona o derivados.")

    def listar_personas(self):
        if not self.personas:
            print("No hay personas en la universidad.")
        else:
            print(f"=== LISTA DE PERSONAS EN {self.nombre} ===")
            for i, persona in enumerate(self.personas, 1):
                print(f"{i}. ", end="")
                persona.mostrar_info()
        return self.personas

    def listar_estudiantes(self):
        # estudiantes = [p for p in self.personas if isinstance(p, Estudiante)]
        estudiantes = []
        for persona in self.personas:
            if isinstance(persona, Estudiante):
                estudiantes.append(persona)
        
        if not estudiantes:
            print("No hay estudiantes en la universidad.")
        else:
            print("=== LISTA DE ESTUDIANTES ===")
            for i, estudiante in enumerate(estudiantes, 1):
                print(f"{i}. ", end="")
                estudiante.mostrar_info()
        return estudiantes

    def listar_profesores(self):
        # profesores = [p for p in self.personas if isinstance(p, Profesor)]
        profesores = []
        for persona in self.personas:
            if isinstance(persona, Profesor):
               profesores.append(persona)
        
        if not profesores:
            print("No hay profesores en la universidad.")
        else:
            print("=== LISTA DE PROFESORES ===")
            for i, profesor in enumerate(profesores, 1):
                print(f"{i}. ", end="")
                profesor.mostrar_info()
        return profesores
    def buscar_estudiante(self, nombre):
        try:
            if not isinstance(nombre, str):
                raise ValueError("El nombre debe ser una cadena de texto.")
            
            for persona in self.personas:
                if isinstance(persona, Estudiante) and persona.nombre.lower() == nombre.lower():
                    print("=== ESTUDIANTE ENCONTRADO ===")
                    persona.mostrar_info()
                    return persona

            print(f"No se encontró ningún estudiante con el nombre: {nombre}")
            return None
        
        except ValueError as e:
            print(f"Error: {e}")
            return None
